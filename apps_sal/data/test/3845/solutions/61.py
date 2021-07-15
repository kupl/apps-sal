# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import fractions
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import Counter
from collections import deque
import pprint
import itertools
from functools import lru_cache

sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# a^n
def power(a, n, mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod


# n*(n-1)*...*(l+1)*l
def kaijo(n, l, mod):
    if n == 0:
        return 1
    a = n
    tmp = n - 1
    while (tmp >= l):
        a = a * tmp % mod
        tmp -= 1
    return a

# Union Find
class UnionFind():
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
            x, y = y, x

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
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# 約数生成
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

# 区間更新のみ
class kukankousin:
    def __init__(self, n):
        self.n = n
        self.N0 = 2**(self.n-1).bit_length()
        self.data = [None]*(2*self.N0)
        self.INF = (-1, 2**31-1)

    # 区間[l, r+1)の値をxに書き換える
    # xは(t, value)という値にする (新しい値ほどtは大きくなる)
    def update(self, l, r, x):
        L=l+self.N0;
        R=r+self.N0
        while L<R:
            if R & 1:
                R-=1
                self.data[R-1]=x

            if L & 1:
                self.data[L-1]=x
                L+=1
            L>>=1;
            R>>=1


    # a_iの現在の値を取得
    def _query(self, k):
        k+=self.N0-1
        s=self.INF
        while k>=0:
            if self.data[k]:
                s=max(s, self.data[k])
            k=(k-1)//2
        return s


    # これを呼び出す
    def query(self, k):
        return self._query(k)[1]


inf = 10 ** 18
mod = 10 ** 9 + 7
# mod = 998244353

# Press the green button in the gutter to run the script.
def __starting_point():
    a,b = lr()
    h,w = 96,99
    m = [['#' for j in range(w)] for i in range(h)]
    for i in range(48,h):
        for j in range(w):
            m[i][j] = '.'

    for k in range(a-1):
        y = k//33
        x = k%33
        y = y*3+1
        x = x*3+1
        m[y][x] = '.'

    for k in range(b-1):
        y = 16+k//33
        x = k%33
        y = y*3+1
        x = x*3+1
        m[y][x] = '#'

    print(h,w)
    for l in m:
        print(*l, sep='')
__starting_point()
