#!/usr/bin/env python3
import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()


N, D = rint()

S = list(rint())
P = list(rint())

new_score = S[D - 1] + P[0]

k = 1
ans = 0
for i in range(D - 2, -1, -1):
    if k > N - 1:
        ans = i + 2
        break
    for j in range(k, N):
        if S[i] + P[j] <= new_score:
            k = j + 1
            break
    else:
        ans = i + 2
        break
else:
    ans = 1
print(ans)
