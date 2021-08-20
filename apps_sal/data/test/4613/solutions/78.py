import sys
sys.setrecursionlimit(10 ** 9)


def int1(x):
    return int(x) - 1


def II():
    return int(input())


def MI():
    return list(map(int, input().split()))


def MI1():
    return list(map(int1, input().split()))


def LI():
    return list(map(int, input().split()))


def LI1():
    return list(map(int1, input().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def MS():
    return input().split()


def LS():
    return list(input())


def LLS(rows_number):
    return [LS() for _ in range(rows_number)]


def printlist(lst, k=' '):
    print(k.join(list(map(str, lst))))


INF = float('inf')
'\nhttps://note.nkmk.me/python-union-find/\n素集合データ構造\n\n:parameter\nunion(x, y): 2つの集合を一つに併合する\nfind(x): xがどの集合に属しているかを判定する\nsize(x): 要素xが属するグループのサイズ（要素数）を返す\nsame(x, y): 要素x, yが同じグループに属するかどうかを返す\nmembers(x): 要素xが属するグループに属する要素をリストで返す\nroots(): 全ての根の要素をリストで返す\ngroup_count(): グループの数を返す\nall_group_members(): 辞書を返す。\u3000key = ルート要素, value = そのグループに含まれる要素のリスト\n__str__(): print()での表示用。ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す\n'


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def all_group_count(self):
        return [self.size(r) for r in self.roots()]

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


def solve():
    (N, M) = MI()
    E = []
    for i in range(M):
        (a, b) = MI1()
        E.append((a, b))
    ans = 0
    for (a, b) in E:
        uf = UnionFind(N)
        for (v1, v2) in E:
            if (v1, v2) == (a, b):
                continue
            uf.union(v1, v2)
        if uf.group_count() > 1:
            ans += 1
    print(ans)


def __starting_point():
    solve()


__starting_point()
