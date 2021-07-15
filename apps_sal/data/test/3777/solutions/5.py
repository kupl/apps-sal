import sys
from operator import itemgetter


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


class LcaDoubling:
    """
    links[v] = { (u, w), (u, w), ... }  (u:隣接頂点, w:辺の重み)
    というグラフ情報から、ダブリングによるLCAを構築。
    任意の2頂点のLCAおよび「パスに含まれる最長辺の長さ」を取得できるようにする
    """

    def __init__(self, n, links, root=0):
        self.depths = [-1] * n
        self.max_paths = [[-1] * (n + 1)]
        self.ancestors = [[-1] * (n + 1)]  # 頂点数より1個長くし、存在しないことを-1で表す。末尾(-1)要素は常に-1
        self._init_dfs(n, links, root)

        prev_ancestors = self.ancestors[-1]
        prev_max_paths = self.max_paths[-1]
        max_depth = max(self.depths)
        d = 1
        while d < max_depth:
            next_ancestors = [prev_ancestors[p] for p in prev_ancestors]
            next_max_paths = [max(prev_max_paths[p], prev_max_paths[q]) for p, q in enumerate(prev_ancestors)]
            self.ancestors.append(next_ancestors)
            self.max_paths.append(next_max_paths)
            d <<= 1
            prev_ancestors = next_ancestors
            prev_max_paths = next_max_paths

    def _init_dfs(self, n, links, root):
        q = [(root, -1, 0, 0)]
        direct_ancestors = self.ancestors[0]
        direct_max_paths = self.max_paths[0]
        while q:
            v, p, dep, max_path = q.pop()
            direct_ancestors[v] = p
            self.depths[v] = dep
            direct_max_paths[v] = max_path
            q.extend((u, v, dep + 1, w) for u, w in links[v] if u != p)
        return direct_ancestors

    def get_lca_with_max_path(self, u, v):
        du, dv = self.depths[u], self.depths[v]
        if du > dv:
            u, v = v, u
            du, dv = dv, du
        tu = u
        tv, max_path = self.upstream(v, dv - du)
        if u == tv:
            return u, max_path
        for k in range(du.bit_length() - 1, -1, -1):
            mu = self.ancestors[k][tu]
            mv = self.ancestors[k][tv]
            if mu != mv:
                max_path = max(max_path, self.max_paths[k][tu], self.max_paths[k][tv])
                tu = mu
                tv = mv
        lca = self.ancestors[0][tu]
        assert lca == self.ancestors[0][tv]
        max_path = max(max_path, self.max_paths[0][tu], self.max_paths[0][tv])
        return lca, max_path

    def upstream(self, v, k):
        i = 0
        mp = 0
        while k:
            if k & 1:
                mp = max(mp, self.max_paths[i][v])
                v = self.ancestors[i][v]
            k >>= 1
            i += 1
        return v, mp


def construct_spanning_tree(n, uvw):
    uft = UnionFind(n)
    spanning_links = [set() for _ in range(n)]
    not_spanning_links = []
    adopted_count = 0
    adopted_weight = 0
    i = 0
    while adopted_count < n - 1:
        u, v, w = uvw[i]
        if uft.find(u, v):
            not_spanning_links.append(uvw[i])
        else:
            spanning_links[u].add((v, w))
            spanning_links[v].add((u, w))
            uft.union(u, v)
            adopted_count += 1
            adopted_weight += w
        i += 1
    not_spanning_links.extend(uvw[i:])
    return adopted_weight, spanning_links, not_spanning_links


def solve(n, m, x, uvw):
    # 最小全域木(MST)のコスト総和がXと一致するなら、MSTに白黒含めれば良い（ただし同率の辺は考慮）
    # そうでないなら、MST以外の辺を使えるのはせいぜい1本まで→各辺の取り替えコスト増加分を見る
    # MST以外の辺(u, v)を採用する際に代わりに除かれる辺は、MST上で{u, v}を結ぶパスの最大コスト辺

    mst_weight, spanning_links, not_spanning_links = construct_spanning_tree(n, uvw)
    # print(mst_weight)
    # print(spanning_links)
    # print(not_spanning_links)
    if x < mst_weight:
        return 0
    diff = x - mst_weight
    lcad = LcaDoubling(n, spanning_links)

    lower_count, exact_count, upper_count = 0, 0, 0
    for u, v, w in not_spanning_links:
        lca, mp = lcad.get_lca_with_max_path(u, v)
        inc = w - mp
        # print(u, v, w, lca, mp, inc)
        if inc < diff:
            lower_count += 1
        elif inc > diff:
            upper_count += 1
        else:
            exact_count += 1

    MOD = 10 ** 9 + 7
    # x >= mst_weight の場合、MSTの辺は全て同じ色として
    # lower_count も全てそれと同じ色
    # exact_count は「全てがMSTと同じ色」でない限りどのような塗り方でもよい
    # upper_count はどのような塗り方でもよい
    replace_to_exact_link = 2 * (pow(2, exact_count, MOD) - 1) * pow(2, upper_count, MOD) % MOD
    if diff > 0:
        return replace_to_exact_link

    # x == mst_weight の場合は、MSTが全て同じ色でない限りどのような塗り方でもよいパターンも追加
    use_first_spanning = (pow(2, n - 1, MOD) - 2) * pow(2, m - n + 1, MOD) % MOD
    return (use_first_spanning + replace_to_exact_link) % MOD


n, m = list(map(int, input().split()))
x = int(input())
uvw = []
for line in sys.stdin:
    u, v, w = list(map(int, line.split()))
    u -= 1
    v -= 1
    uvw.append((u, v, w))
uvw.sort(key=itemgetter(2))
print((solve(n, m, x, uvw)))

