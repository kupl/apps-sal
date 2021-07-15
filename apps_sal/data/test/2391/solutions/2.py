#!/usr/bin/env python3
import sys
input = sys.stdin.readline

class RollingHash():
    def __init__(self, s):
        self.length = len(s)
        self.base = 1009
        self.mod = (1 << 61) - 1
        self.hash = [0] * (self.length + 1)
        self.pow = [1] * (self.length + 1)

        for i in range(self.length):
            self.hash[i+1] = (self.hash[i] + s[i]) * self.base % self.mod
            self.pow[i+1] = self.pow[i] * self.base % self.mod

    def get(self, l, r):
        t = self.hash[r] - self.hash[l] * self.pow[r-l] % self.mod
        t = (t + self.mod) % self.mod
        return t

n = int(input())
a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]
a = a + a

diffa = []
diffb = []
for i in range(1, len(a)):
    diffa.append(a[i] ^ a[i-1])
for i in range(1, len(b)):
    diffb.append(b[i] ^ b[i-1])

RHa = RollingHash(diffa)
RHb = RollingHash(diffb)
query = RHb.get(0, n-1)
ans = []
for i in range(n):
    val = RHa.get(i, i+n-1)
    if val == query:
        ans.append((i, a[i] ^ b[0]))
ans.sort()
for k, x in ans:
    print(k, x)
