from collections import Counter, deque
import bisect
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")
MOD = 10**9 + 7

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    class UnionFind:
        def __init__(self, n):
            self.par = [i for i in range(n + 1)]
            self.rank = [0] * (n + 1)
            self.size = [1] * (n + 1)

        def find(self, x):
            if self.par[x] == x:
                return x
            else:
                self.par[x] = self.find(self.par[x])
                return self.par[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.rank[x] < self.rank[y]:
                self.par[x] = y
                self.size[y] += self.size[x]
                self.size[x] = 0
            else:
                self.par[y] = x
                self.size[x] += self.size[y]
                self.size[y] = 0
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def all_find(self):
            for n in range(len(self.par)):
                self.find(n)

    N, M, K = i_map()
    tree = UnionFind(N)
    not_friend_candi = []

    for i in range(M):
        A, B = i_map()
        A -= 1
        B -= 1
        tree.union(A, B)
        not_friend_candi.append([A, B])

    tree.all_find()

    for j in range(K):
        C, D = i_map()
        C -= 1
        D -= 1
        not_friend_candi.append([C, D])

    ans = [0] * N
    for i, j in not_friend_candi:
        if tree.same(i, j):
            ans[i] -= 1
            ans[j] -= 1
    for i in range(N):
        p = tree.find(i)
        ans[i] += tree.size[p] - 1
    print(*ans)


def __starting_point():
    main()


__starting_point()
