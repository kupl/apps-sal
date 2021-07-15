import sys
import numpy as np
INF = 10**18+5
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = np.sort(a)
    ap = a[a > 0]
    an = a[a < 0]
    zc = n * (n - ap.size - an.size)

    l = -INF
    r = INF
    while(l+1 < r):
        x = (l+r)//2

        total = (n-np.searchsorted(a, -(-x // an), side='left')).sum()
        if x >= 0:
            total += zc
        total += np.searchsorted(a, x // ap, side='right').sum()
        total -= a[a*a <= x].size
        total //= 2
        if total < k:
            l = x
        else:
            r = x

    print(r)


main()

