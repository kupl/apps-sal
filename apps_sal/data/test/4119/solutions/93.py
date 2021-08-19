(N, M) = map(int, input().split())
X = list(map(int, input().split()))
X = sorted(X, reverse=False)
if len(X) == 1:
    print(0)
else:
    dist = []
    for i in range(1, M):
        dist.append(X[i] - X[i - 1])
    dist = sorted(dist, reverse=False)
    for k in range(N - 1):
        dist.pop()
        if len(dist) == 0:
            break
    print(sum(dist))
