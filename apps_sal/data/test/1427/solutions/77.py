import sys
import math
import fractions
from collections import defaultdict
from functools import reduce
import collections
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return map(int, stdin.readline().split())


def nl():
    return list(map(int, stdin.readline().split()))


INF = 10 ** 18
mod = 10 ** 9 + 7
N = int(input())
A = nl()
NMAX = 10 ** 6


class Sieve:

    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)
        self.prime = []
        self.f[0] = self.f[1] = -1
        for i in range(2, n + 1):
            if self.f[i]:
                continue
            else:
                self.prime.append(i)
                self.f[i] = i
                for j in range(i * i, n + 1, i):
                    if ~self.f[j]:
                        self.f[j] = i

    def isProme(self, x):
        return self.f[x] == x

    def factorList(self, x):
        res = []
        while x != 1:
            res.append(self.f[x])
            x //= self.f[x]
        return res

    def factor(self, x):
        fl = self.factorList(x)
        return collections.Counter(fl)


def get_sieve_of_eratosthenes(n):
    prime = [2]
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


sieve = Sieve(10 ** 6)
mp = defaultdict(int)
for i in range(N):
    f = sieve.factor(A[i])
    for (key, val) in f.items():
        mp[key] = max(val, mp[key])
lcm = 1
for (key, val) in mp.items():
    lcm *= key ** val
ans = 0
for i in range(N):
    ans += lcm // A[i]
print(ans % mod)
