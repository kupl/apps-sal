from math import atan2


def skal(a, b):
    return a[0][0] * b[0][0] + a[0][1] * b[0][1]


def vect(a, b):
    return a[0][0] * b[0][1] - b[0][0] * a[0][1]


n = int(input())
a = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append([[x, y], i + 1])
a.sort(key=lambda x: atan2(x[0][1], x[0][0]))
a.append(a[0])
c = [[skal(a[0], a[1]), abs(vect(a[0], a[1]))], [a[0][1], a[1][1]]]
for i in range(1, n):
    d = [[skal(a[i], a[i + 1]), abs(vect(a[i], a[i + 1]))], [a[i][1], a[i + 1][1]]]
    if vect(d, c) > 0:
        c = d
print(c[1][0], c[1][1])
