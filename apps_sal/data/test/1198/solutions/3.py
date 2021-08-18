from functools import *
from time import time
from heapq import *


def main():
    n, c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    if c > n:
        print(sum(a))
        return

    b = n * [0]
    s = 0
    h = []
    for i in range(n):
        s = s + a[i] if i <= c - 1 else s + a[i] - a[i - c]
        heappush(h, (a[i], i))
        if i <= c - 2:
            b[i] = s
        else:
            while i - h[0][1] >= c:
                heappop(h)
            v1 = b[i - c] + s - h[0][0]
            v2 = a[i] + b[i - 1]
            b[i] = min(v1, v2)

    print(b[-1])


def __starting_point():
    main()


__starting_point()
