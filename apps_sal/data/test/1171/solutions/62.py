(N, K) = map(int, input().split())
V = list(map(int, input().split()))
M = min(N, K)
ans = 0
for i in range(M + 1):
    for j in range(M - i + 1):
        G = V[:i] + V[N - j:]
        G.sort()
        for j in range(K - i - j + 1):
            ans = max(ans, sum(G[j:]))
print(ans)
