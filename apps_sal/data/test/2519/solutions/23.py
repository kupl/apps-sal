N, K = map(int, input().split())
P = list(map(int, input().split()))
ls = [0] * (N + 1)

for i in range(N):
    ls[i + 1] += ls[i] + (P[i] + 1) / 2

ans = 0
for j in range(N - K + 1):
    tmp = ls[K + j] - ls[j]
    ans = max(ans, tmp)

print(ans)
