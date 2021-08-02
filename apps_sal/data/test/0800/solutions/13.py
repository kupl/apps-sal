from sys import stdin
import functools
import math


def read(): return list(map(int, stdin.readline().split()))


n, = read()
a = []
for i in range(n):
    x, y = read()
    a.append(math.atan2(y, x) % (2 * math.pi))
a = sorted(a)

if abs(a[0] - a[-1]) < 1e-9:
    print(0)
    return

ans = 0
for i in range(n):
    ans = max(ans, a[i] - a[i - 1])
ans = max(ans, 2 * math.pi - (a[-1] - a[0]))

print(360.0 - ans / math.pi * 180.0)
