from math import atan2


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


n = int(input())
a = []
for i in range(0, n):
    [x, y] = map(int, input().split())
    a.append([i + 1, [x, y]])
a.sort(key=lambda x: atan2(x[1][0], x[1][1]))
a.append(a[0])
for i in range(1, len(a)):
    a[i - 1].append([dot(a[i - 1][1], a[i][1]), abs(cross(a[i - 1][1], a[i][1]))])
best = a[0]
ma = [a[0][0], a[1][0]]
for i in range(1, len(a)):
    if cross(a[i][2], best[2]) > 0:
        best = a[i]
        ma = [a[i][0], a[i + 1][0]]
print(ma[0], ma[1])
