import math


def arg(x, y):
    if x == 0:
        if y > 0:
            return math.pi / 2
        else:
            return 3 * math.pi / 2
    elif x > 0:
        return math.atan(y / x)
    else:
        return math.atan(y / x) + math.pi


n = int(input())
A = []
for i in range(n):
    (x, y) = map(int, input().split())
    if x == 0 and y == 0:
        continue
    A.append([arg(x, y), x, y])
    A.append([arg(x, y) + 2 * math.pi, x, y])
A = sorted(A)
n = len(A) // 2
ans = 0
for i in range(n):
    for j in range(1, n + 1):
        X = 0
        Y = 0
        for k in range(i, i + j):
            X = X + A[k][1]
            Y = Y + A[k][2]
        d = (X ** 2 + Y ** 2) ** (1 / 2)
        if d > ans:
            ans = d
print(ans)
