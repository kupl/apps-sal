import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
MOD = 10**9 + 7
N, K = map(int, input().split())
ans = [0] * K
for i in range(K):
    p = K - i
    a = pow(math.floor(K / p), N, MOD)
    x = 1
    while p * (x + 1) <= K:
        a -= ans[p * (x + 1) - 1]
        x = x + 1
    ans[p - 1] = a % MOD
s = 0
for i in range(K):
    s += (i + 1) * ans[i]
    s = s % MOD
print(s)
