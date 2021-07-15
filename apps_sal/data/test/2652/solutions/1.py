import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return list(map(int, input().split()))
def read_index(): return [int(x) - 1 for x in input().split()]
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class UF:
    def __init__(self, N):
        self.state = [-1] * N
        self.rank = [0] * N
        self.num_group = N
    
    def get_parent(self, a):
        p = self.state[a]
        if p < 0:
            return a
        
        q = self.get_parent(p)
        self.state[a] = q
        return q

    def make_pair(self, a, b):
        pa = self.get_parent(a)
        pb = self.get_parent(b)
        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            pa, pb = pb, pa
            a, b = b, a
        elif self.rank[pa] == self.rank[pb]:
            self.rank[pb] += 1

        self.state[pb] += self.state[pa]
        self.state[pa] = pb
        self.state[a] = pb
        self.num_group -= 1
    
    def is_pair(self, a, b):
        return self.get_parent(a) == self.get_parent(b)

    def get_size(self, a):
        return -self.state[self.get_parent(a)]


def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        a, b = read_values()
        X.append((a, i))
        Y.append((b, i))
    
    X.sort()
    Y.sort()

    Q = []
    for i in range(N - 1):
        heapq.heappush(Q, (X[i + 1][0] - X[i][0], (X[i][1], X[i + 1][1])))
        heapq.heappush(Q, (Y[i + 1][0] - Y[i][0], (Y[i][1], Y[i + 1][1])))

    res = 0
    uf = UF(N)
    while uf.num_group != 1:
        c, (a, b) = heapq.heappop(Q)

        if not uf.is_pair(a, b):
            res += c
            uf.make_pair(a, b)

    print(res)


def __starting_point():
    main()


__starting_point()
