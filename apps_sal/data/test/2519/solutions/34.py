N, K = map(int, input().split())
P = [(int(x) + 1) / 2 for x in input().split()]

Q = [0] * (N + 1)
for n in range(N):
    Q[n + 1] = Q[n] + P[n]

ans = 0
for n in range(K, N + 1):
    ans = max(ans, Q[n] - Q[n - K])

print(ans)
