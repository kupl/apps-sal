# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

"""
全体からあまりがK未満を引く
"""
N, K = lr()
total = N * N
for b in range(1, N+1):
    if b <= K:
        total -= N
    else:
        total -= K * (N // b) + max(0, min(N % b, K - 1))
    #print(b, total)

answer = total
print(answer)

