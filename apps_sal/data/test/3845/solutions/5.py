import sys
import math
import copy
import random
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

input = sys.stdin.readline
def getS(): return input().strip()
def getN(): return int(input())
def getList(): return list(map(int, input().split()))
def getZList(): return [int(x) - 1 for x in input().split()]


INF = float("inf")
MOD = 10**9 + 7
def divide(x): return pow(x, MOD - 2, MOD)


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n - k])) % MOD


def fact_and_inv(SIZE):
    inv = [0] * SIZE
    fac = [0] * SIZE
    finv = [0] * SIZE
    inv[1] = 1
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, SIZE):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return fac, finv


def renritsu(A, Y):
    A = np.matrix(A)
    Y = np.matrix(Y)
    Y = np.reshape(Y, (-1, 1))
    X = np.linalg.solve(A, Y)

    return X.flatten().tolist()[0]


class TwoDimGrid:
    def __init__(self, h, w, wall="
        self.h=h
        self.w=w
        self.size=(h + 2) * (w + 2)
        self.wall=wall
        self.get_grid()

    def get_grid(self):
        grid = [self.wall * (self.w + 2)]
        for i in range(self.h):
            grid.append(self.wall + getS() + self.wall)

        grid.append(self.wall * (self.w + 2))
        self.grid = grid

    def init_cost(self):
        self.cost = [INF] * self.size

    def pos(self, x, y):
        return y * (self.w + 2) + x

    def getgrid(self, x, y):
        return self.grid[y][x]

    def get(self, x, y):
        return self.cost[self.pos(x, y)]

    def set(self, x, y, v):
        self.cost[self.pos(x, y)] = v
        return

    def show(self):
        for i in range(self.h + 2):
            print(self.cost[(self.w + 2) * i:(self.w + 2) * (i + 1)])

    def showsome(self, tgt):
        for t in tgt:
            print(t)
        return

    def showsomejoin(self, tgt):
        for t in tgt:
            print("".join(t))
        return

    def search(self):
        grid = self.grid
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move_eight = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def solve():
    a, b=getList()
    print(100, 100)
    for i in range(100):
        tmp = []
        for j in range(100):
            if i < 50:
                if j % 2 == 1 or i % 2 == 1 or a <= 1:
                    tmp.append("
                else:
                    tmp.append(".")
                    a -= 1
            else:
                if j % 2 == 1 or i % 2 == 0 or b <= 1:
                    tmp.append(".")
                else:
                    tmp.append("
                    b -= 1

        print("".join(tmp))


def main():
    n=getN()
    for _ in range(n):
        s="".join([random.choice(["F", "T"]) for i in range(20)])
        print(s)
        solve(s, 1, 0)

    return


def __starting_point():
    solve()


__starting_point()
