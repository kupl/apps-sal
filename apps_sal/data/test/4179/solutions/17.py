#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc121/tasks/abc121_b

N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0

for i in range(N):
    y = 0
    for j in range(M):
        y += A[i][j] * B[j]
    y += C

    if y > 0:
        ans += 1

print(ans)
