from math import *
n = int(input())
r = [list(map(int, input().split())) for _ in range(n)]
ans = 10 ** 20
for i in range(n):
    x0, y0 = r[(i + n - 1) % n]
    x1, y1 = r[(i + 1) % n]
    x, y = r[i]
    ans = min(ans, abs((y1 - y0) * x - (x1 - x0) * y - (x0 * y1 - x1 * y0)) / sqrt((x1 - x0)**2 + (y1 - y0)**2))
print(ans / 2)
