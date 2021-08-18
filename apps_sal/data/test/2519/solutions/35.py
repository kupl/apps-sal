N, K = map(int, input().split())
p = list(map(int, input().split()))

for i in range(N):
    p[i] = (1 + p[i]) / 2

S = [0] * N
S[0] = p[0]
for i in range(N - 1):
    S[i + 1] = S[i] + p[i + 1]

ans = S[K - 1]
for i in range(N - K):
    ans = max(ans, S[i + K] - S[i])

print(ans)
