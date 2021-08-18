from sys import stdin
import math
from collections import defaultdict

input = stdin.readline


n = int(input())
l = list(map(int, input().split(" ")))

k = math.ceil(math.log2(n))
dp = [[0] * k for i in range(2 ** k)]


def make_sparse(l, n, k):
    """Making sparse table, replace max with needed function like[GCD, Min, max, sum]"""
    for i in range(n):
        dp[i][0] = l[i]

    for j in range(1, k + 1):
        i = 0
        while i + (1 << j) <= n:
            dp[i][j] = math.gcd(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1])
            i += 1


def querys(l, r):
    j = int(math.log2(r - l + 1))
    return math.gcd(dp[l][j], dp[r - (1 << j) + 1][j])


make_sparse(l, n, k)
d = defaultdict(int)
g = defaultdict(int)
d[l[0]] = 1
g[l[0]] = 1
for i in range(1, n):
    t = defaultdict(int)
    t[l[i]] = 1
    g[l[i]] += 1
    for k, v in list(d.items()):
        gcd = math.gcd(k, l[i])
        t[gcd] += v
        g[gcd] += v
    d = t

for i in range(int(input())):
    a = g[int(input())]
    if not a:
        print(0)
    else:
        print(a)
