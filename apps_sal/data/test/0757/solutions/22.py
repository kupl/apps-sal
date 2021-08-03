from sys import stdin
import functools
import math


def read(): return list(map(int, stdin.readline().split()))


_, dev, sockets = read()

dev -= sockets
a = sorted(list(read()))
ans = 0
while dev > 0 and len(a) > 0:
    dev -= a.pop() - 1
    ans += 1

if dev > 0:
    print("-1")
else:
    print(ans)
