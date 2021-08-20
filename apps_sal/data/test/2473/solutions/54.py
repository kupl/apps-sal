import sys
stdin = sys.stdin


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def nn():
    return list(stdin.readline().split())


def ns():
    return stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 6)
(n, k) = na()
xy = []
for i in range(n):
    (x, y) = na()
    xy.append((x, y))
xy.sort()
ans = 10000000000000000000000000000
for i in range(n):
    for j in range(i + 1, n):
        x = xy[j][0] - xy[i][0]
        yy = sorted(xy[i:j + 1], key=lambda x: x[1])
        for u in range(len(yy) - k + 1):
            y = yy[u + k - 1][1] - yy[u][1]
            ans = min(ans, y * x)
print(ans)
