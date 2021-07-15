import math

N, D = map(int, input().split())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0
for i in range(N):
    distance = math.sqrt(X[i] ** 2 + Y[i] ** 2)
    if distance <= D:
        ans += 1
print(ans)
