import sys

N, X, Y = map(int, sys.stdin.readline().split())

ans = [0] * (N - 1)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        k = min((j - i, abs(X - i) + 1 + abs(j - Y), abs(X - j) + 1 + abs(i - Y)))
        ans[k - 1] += 1

for i in range(N - 1):
    print(ans[i])
