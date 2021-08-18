from itertools import count, permutations, chain
from pprint import pprint
from collections import deque, defaultdict
from functools import lru_cache
from math import gcd
import math
import sys
sys.setrecursionlimit(1000000000)
def lcm(a, b): return a * b // gcd(a, b)


def ii(): return int(input())
def mis(): return list(map(int, input().split()))
def lmis(): return list(mis())


INF = float('inf')
N1097 = 10**9 + 7


def meg(f, ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok


def get_inv(n, modp):
    return pow(n, modp - 2, modp)


def factorials_list(n, modp):
    fs = [1]
    for i in range(1, n + 1):
        fs.append(fs[-1] * i % modp)
    return fs


def invs_list(n, fs, modp):
    invs = [get_inv(fs[-1], modp)]
    for i in range(n, 1 - 1, -1):
        invs.append(invs[-1] * i % modp)
    invs.reverse()
    return invs


def comb(n, k, modp):
    num = 1
    for i in range(n, n - k, -1):
        num = num * i % modp
    den = 1
    for i in range(2, k + 1):
        den = den * i % modp
    return num * get_inv(den, modp) % modp


def comb_from_list(n, k, modp, fs, invs):
    return fs[n] * invs[n - k] * invs[k] % modp


class UnionFindEx:
    def __init__(self, size):
        self.roots = [-1] * size

    def getRootID(self, i):
        r = self.roots[i]
        if r < 0:
            return i
        else:
            r = self.getRootID(r)
            self.roots[i] = r
            return r

    def getGroupSize(self, i):
        return -self.roots[self.getRootID(i)]

    def connect(self, i, j):
        r1, r2 = self.getRootID(i), self.getRootID(j)
        if r1 == r2:
            return False
        if self.getGroupSize(r1) < self.getGroupSize(r2):
            r1, r2 = r2, r1
        self.roots[r1] += self.roots[r2]
        self.roots[r2] = r1
        return True


Yes = 'Yes'
No = 'No'


def main():
    N = ii()
    up = []
    down = []
    for _ in range(N):
        S = input()
        h = 0
        b = 0
        for s in S:
            if s == '(':
                h += 1
            else:
                h -= 1
                b = min(b, h)
        if h >= 0:
            up.append((h, b))
        else:
            down.append((h, b))
    up.sort(key=lambda t: t[1], reverse=True)
    down.sort(key=lambda t: t[0] - t[1], reverse=True)
    H = 0
    for h, b in up:
        if H + b >= 0:
            H += h
        else:
            print(No)
            return
    for h, b in down:
        if H + b >= 0:
            H += h
        else:
            print(No)
            return
    if H == 0:
        print(Yes)
    else:
        print(No)


main()
