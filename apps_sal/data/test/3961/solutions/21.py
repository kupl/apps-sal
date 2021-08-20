"""input
4
1 1 2 3
"""
from sys import stdin, stdout
import sys
sys.setrecursionlimit(15000)
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
dp[1] = 2
mod = 10 ** 9 + 7
for i in range(2, n + 1):
    dp[i] = (sum(dp[arr[i - 1]:i]) + 2) % mod
print(sum(dp[1:]) % (10 ** 9 + 7))
