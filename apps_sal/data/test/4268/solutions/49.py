import math
(N, D) = map(int, input().split())
coordinates = []
ans = 0
for _ in range(N):
    X = list(map(int, input().split()))
    coordinates.append(X)
for i in range(N):
    for j in range(i + 1, N):
        dist = 0
        for k in range(D):
            dist += (coordinates[i][k] - coordinates[j][k]) ** 2
        dist = math.sqrt(dist)
        if dist == dist // 1:
            ans += 1
print(ans)
