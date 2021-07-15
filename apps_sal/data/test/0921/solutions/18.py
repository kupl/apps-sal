import sys
from itertools import accumulate

def solve():
    n, w = map(int, input().split())

    a = [int(i) for i in input().split()]
    b = [0] * n

    for i, ai in enumerate(a):
        tmp = (ai + 1) // 2

        w -= tmp
        b[i] += tmp

        if w < 0:
            print(-1)
            return

    ag = [(ai, i) for i, ai in enumerate(a)]
    ag.sort(reverse=True)

    for i in range(n):
        v = ag[i][0]
        k = ag[i][1]
        rem = v - b[k]

        if w > rem:
            w -= rem
            b[k] = v
        else:
            b[k] += w
            break

    print(*b)

def __starting_point():
    solve()
__starting_point()
