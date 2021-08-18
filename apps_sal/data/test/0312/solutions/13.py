n, m = (int(i) for i in input().split())


def solve():
    if n == 1:
        return 1

    a1 = m - 1
    a2 = m + 1
    if a1 < 1:
        return a2

    if a2 > n:
        return a1

    b1 = a1
    b2 = n - a2 + 1
    return a1 if b1 >= b2 else a2


print(solve())
