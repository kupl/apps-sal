import sys
from itertools import accumulate

def solve():
    def check(m):
        if m == 0:
            return 0

        b = [ai + (i + 1)*m for i, ai in enumerate(a)]
        b.sort()

        return sum(b[:m])

    n, S = map(int, input().split())
    a = [int(i) for i in input().split()]

    btm = -1
    top = n + 1

    while top - btm > 1:
        mid = (top + btm) // 2

        if check(mid) <= S:
            btm = mid
        else:
            top = mid

    k = btm
    T = check(k)

    print(k, T)

def __starting_point():
    solve()
__starting_point()
