import sys
from itertools import accumulate
from operator import or_

inf = float('inf')


def solve():
    n, m = map(int, input().split())
    s = [[int(j) for j in input()] for i in range(n)][::-1]

    e = [any(si) for si in s]
    es = e[:] + [False]
    es = list(accumulate(es[::-1], or_))[::-1]

    if not es[0]:
        print(0)
    else:
        lim = 0

        for i in range(n + 1):
            if not es[i]:
                lim = i - 1
                break

        left, right = -1, inf

        for i in range(lim):
            if not e[i]:
                left, right = min(left + 1, right + m + 2), min(right + 1, left + m + 2)
            else:
                kr = rindex(s[i], 1)
                kl = s[i].index(1)
                left, right = min(left + 1 + 2 * kr, right + m + 2), min(right + 1 + 2 * (m + 1 - kl), left + m + 2)

        kr = rindex(s[lim], 1)
        kl = s[lim].index(1)

        ans = min(left + 1 + kr, right + m + 2 - kl)

        print(ans)


def rindex(arr, x):
    return len(arr) - 1 - arr[::-1].index(x)


def __starting_point():
    solve()


__starting_point()
