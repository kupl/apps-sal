from collections import deque
import sys


def inp():
    return sys.stdin.readline().strip()


for _ in range(int(inp())):
    n, k = list(map(int, inp().split()))
    a = list(map(int, inp().split()))
    d = {}
    f = 0
    mx = -1
    for i in a:
        if i % k == 0:
            continue
        if i % k not in d:
            d[i % k] = 0
        d[i % k] += 1
        if f < d[i % k]:
            f = d[i % k]
            mx = i % k
        elif f == d[i % k]:
            mx = min(mx, i % k)
    if mx == -1:
        print(0)
        continue
    print((f - 1) * k + (k - mx) + 1)
