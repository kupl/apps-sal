import collections


def readLine():
    return list(map(int, input().strip().split()))


def readInt():
    return int(input())


def readString():
    return input()


def tcase():
    t = readInt()
    for _ in range(t):
        solve()


def solve():
    n = readInt()
    (lo, hi) = (1, n)
    while lo < hi:
        mid = lo + hi + 1 >> 1
        if mid * (mid + 1) // 2 <= n + 1:
            lo = mid
        else:
            hi = mid - 1
    print(n - lo + 1)


solve()
