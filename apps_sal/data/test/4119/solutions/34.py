(N, M) = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
dist = [0] * (M - 1)
for i in range(0, M - 1):
    dist[i] += X[i + 1] - X[i]
dist.sort(reverse=True)
print(sum(dist[N - 1:]))
