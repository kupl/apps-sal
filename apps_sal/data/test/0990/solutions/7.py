from functools import reduce
# https://drken1215.hatenablog.com/entry/2020/01/26/164200
# bit_pathの参考にした
# https://atcoder.jp/contests/abc152/submissions/9619555
# popcnt

def main():
    from collections import namedtuple
    from functools import reduce
    from itertools import combinations
    from operator import or_

    Edge = namedtuple('Edge', 'to edge_id')

    def bit_path(curr, goal, par=-1):
        if curr == goal:
            return 0
        for e in g[curr]:
            if e.to == par: continue
            res = bit_path(curr=e.to, goal=goal, par=curr)
            if ~res:  # -1以外
                return res | (1 << e.edge_id)
        return -1

    def popcnt(n):
        """https://atcoder.jp/contests/abc152/submissions/9619555"""
        c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
        c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
        c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
        c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
        c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
        c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
        return c

    N = int(input())

    g = tuple(set() for _ in range(N))
    for edge_id in range(N - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].add(Edge(to=b, edge_id=edge_id))
        g[b].add(Edge(to=a, edge_id=edge_id))

    M = int(input())

    cons = []
    for _ in range(M):
        u, v = (int(x) - 1 for x in input().split())
        b = bit_path(u, v)
        cons.append(b)

    ans = 1 << (N - 1)
    for k in range(1, M + 1):
        for comb in combinations(cons, r=k):
            b = reduce(or_, comb)
            ans += ((-1) ** k) * (1 << (N - 1 - popcnt(b)))
    print(ans)


def __starting_point():
    main()

__starting_point()
