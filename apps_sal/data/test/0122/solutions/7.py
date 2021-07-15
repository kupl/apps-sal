import sys
from itertools import accumulate

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    S = sum(a)

    if S & 1:
        print('NO')
        return

    S //= 2

    ap = set()
    ps = [0] + list(accumulate(a))

    for i in range(1, n + 1):
        x = ps[i] - S
        ap.add(a[i - 1])

        if x == 0 or x in ap:
            print('YES')
            return

    ap = set()
    a = a[::-1]
    ps = [0] + list(accumulate(a))

    for i in range(1, n + 1):
        x = ps[i] - S
        ap.add(a[i - 1])

        if x == 0 or x in ap:
            print('YES')
            return

    print('NO')

def __starting_point():
    solve()
__starting_point()
