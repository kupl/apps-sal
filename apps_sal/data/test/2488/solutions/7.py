import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, d, a) = list(map(int, input().split()))
    XH = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    res = 0
    total = 0
    end = deque([])
    for i in range(n):
        (x, h) = XH[i]
        while end and end[0][0] < x:
            r = end.popleft()
            total -= r[1]
        if total < h:
            res += (h - total + a - 1) // a
            damage = (h - total + a - 1) // a * a
            total += damage
            end.append([x + 2 * d, damage])
    print(res)


def __starting_point():
    resolve()


__starting_point()
