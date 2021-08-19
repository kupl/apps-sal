import math
N = int(input())
X = []
for _ in range(N):
    (x, y) = map(int, input().split())
    X.append((math.atan2(x, y), x, y))
X = sorted(X) * 2
ma = 0
for i in range(N):
    sx = sy = 0
    for j in range(i, i + N):
        sx += X[j][1]
        sy += X[j][2]
        d = sx ** 2 + sy ** 2
        ma = max(ma, d)
print(ma ** 0.5)
