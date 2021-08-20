import math
(N, D) = map(int, input().split())
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]
Distance = []
ans = 0
Distance = 0
for i in range(N):
    (X[i], Y[i]) = map(int, input().split())
    Distance = math.sqrt(X[i] ** 2 + Y[i] ** 2)
    if Distance <= D:
        ans += 1
print(ans)
