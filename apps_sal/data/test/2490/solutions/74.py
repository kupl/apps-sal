# coding: utf-8
import sys


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = sr()
dp = [0, 1]  # ちょうど払う最小枚数、１円多くはらう最小枚数
for x in N:
    x = int(x)
    prev = dp[:]
    dp[0] = min(prev[0] + x, prev[1] + (10 - x))
    dp[1] = min(prev[0] + x + 1, prev[1] + (10 - x - 1))

answer = dp[0]
print(answer)
# 33
