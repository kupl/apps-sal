from math import sqrt, factorial, gcd, log2, inf, ceil
from heapq import heapify, heappush, heappop
from sys import stdin, stdout
import heapq
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right
import sys
from sys import stdin
from collections import deque
mod = 10 ** 9 + 7


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
l = list(map(int, input().split()))


def solve(n):
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            hash[n].add(i)
            hash[n].add(n // i)
    hash[n] = sorted(list(hash[n]))[::-1]


hash = defaultdict(set)
dp = [0] * (10 ** 6 + 1)
dp[0] = 1
for i in l:
    if hash[i] == set():
        solve(i)
        for j in hash[i]:
            dp[j] = dp[j] % mod + dp[j - 1] % mod
            dp[j] %= mod
    else:
        for j in hash[i]:
            dp[j] = dp[j] % mod + dp[j - 1] % mod
            dp[j] %= mod
print(sum(dp[1:]) % mod)
