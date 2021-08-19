import collections


def f():
    (n, m) = [int(c) for c in input().split()]
    if m > n // 2:
        return max(1, m - 1)
    return min(n, m + 1)


print(f())
