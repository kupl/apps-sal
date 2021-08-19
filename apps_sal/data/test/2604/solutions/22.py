from math import sqrt


def dist(x1, y1):
    return sqrt(x1 * x1 + y1 * y1)


(r, d) = list(map(int, input().split()))
n = int(input())
res = 0
for i in range(n):
    (x, y, i) = list(map(int, input().split()))
    if dist(x, y) - i >= r - d and dist(x, y) + i <= r:
        res += 1
print(res)
