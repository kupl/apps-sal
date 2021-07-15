import sys
from itertools import accumulate

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    S = sum(a)

    if S & 1:
        print('NO')
        return

    f_a = dict()
    l_a = dict()

    for i in range(n):
        if a[i] not in f_a:
            f_a[a[i]] = i

    for i in range(n - 1, -1, -1):
        if a[i] not in l_a:
            l_a[a[i]] = i

    ps = [0] + list(accumulate(a))
    S //= 2

    for k in range(1, n + 1):
        x = S - ps[k]

        if x == 0:
            print('YES')
            return
        elif x > 0:
            if x in l_a and k <= l_a[x]:
                print('YES')
                return
        else:
            x *= -1
            
            if x in f_a and f_a[x] < k:
                print('YES')
                return

    print('NO')


def __starting_point():
    solve()
__starting_point()
