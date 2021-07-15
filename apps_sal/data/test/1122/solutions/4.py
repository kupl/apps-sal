
from itertools import count, permutations, chain
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint
import sys
sys.setrecursionlimit(1000000000)
import math
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
ii = lambda: int(input())
mis = lambda: list(map(int, input().split()))
lmis = lambda: list(mis())
INF = float('inf')
N1097 = 10**9 + 7

def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok

def get_inv(n, modp):
    return pow(n, modp-2, modp)

def factorials_list(n, modp):    # 10**6
    fs = [1]
    for i in range(1, n+1):
        fs.append(fs[-1] * i % modp)
    return fs

def invs_list(n, fs, modp):     # 10**6
    invs = [get_inv(fs[-1], modp)]
    for i in range(n, 1-1, -1):
        invs.append(invs[-1] * i % modp)
    invs.reverse()
    return invs

def comb(n, k, modp):
    num = 1
    for i in range(n, n-k, -1):
        num = num * i % modp
    den = 1
    for i in range(2, k+1):
        den = den * i % modp
    return num * get_inv(den, modp) % modp

def comb_from_list(n, k, modp, fs, invs):   
    return fs[n] * invs[n-k] * invs[k] % modp

#

class UnionFindEx:
    def __init__(self, size):
        #正なら根の番号、負ならグループサイズ
        self.roots = [-1] * size
    def getRootID(self, i):
        r = self.roots[i]
        if r < 0:   #負なら根
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
        self.roots[r1] += self.roots[r2]    #サイズ更新
        self.roots[r2] = r1
        return True

Yes = 'Yes'
No = 'No'


def main():
    N, M = mis()
    if N&1:
        q = deque(list(range(M*2)))
        while q:
            print((q.popleft()+1, q.pop()+1))
    else:
        q1 = deque(list(range(N)))
        q2 = deque(list(range(N-1)))
        p1 = []
        while q1:
            p1.append((q1.popleft()+1, q1.pop()+1))
        p2 = []
        while len(q2)>=2:
            p2.append((q2.popleft()+1, q2.pop()+1))
        p2.reverse()
        for _ in range(M):
            print((*p1.pop()))
            p1, p2 = p2, p1


main()


