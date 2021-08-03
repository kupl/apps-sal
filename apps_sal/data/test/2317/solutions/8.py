from math import sqrt, fabs


def dist(x1, y1, x2, y2):
    return sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))


def calcOptimumRightPoint(startX, startY):
    l = float("inf")
    idx = -1
    for i in range(len(B)):
        d = dist(startX, startY, b, B[i]) + L[i]
        if d <= l:
            l = d
            idx = i
    return idx


n, m, a, b = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

optimumRightPoint = calcOptimumRightPoint(0, 0)

intersectLeft = (a * B[optimumRightPoint]) / b

l = float("inf")
optimumLeftPoint = -1
for i in range(len(A)):
    if fabs(intersectLeft - A[i]) < l:
        l = fabs(intersectLeft - A[i])
        optimumLeftPoint = i

optimumRightPoint = calcOptimumRightPoint(a, A[optimumLeftPoint])

print(optimumLeftPoint + 1, optimumRightPoint + 1)
