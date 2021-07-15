#!/usr/bin/env python3
N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [0] * M
X = [0] * M
for i in range(M):
    P[i], X[i] = list(map(int, input().split()))

for i in range(M):
    ans = 0
    ans += sum(T[:P[i] - 1])
    ans += X[i]
    ans += sum(T[P[i]:])
    print(ans)

