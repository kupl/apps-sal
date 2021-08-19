from heapq import *


def f():
    return map(int, input().split())


(n, c) = f()
a = list(f()) + [0] * c
b = [0] * (n + c)
s = 0
h = [(0, -1)]
for i in range(n):
    s += a[i] - a[i - c]
    heappush(h, (a[i], i))
    while h[0][1] <= i - c:
        heappop(h)
    b[i] = min(b[i - 1] + a[i], b[i - c] + s - h[0][0])
print(b[n - 1])
