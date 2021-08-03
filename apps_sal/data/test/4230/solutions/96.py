def ri():
    return int(input())


def rii():
    return [int(v) for v in input().split()]


def solve():
    X, N = rii()
    P = set(rii())
    n = m = float("inf")
    if not P:
        print(X)
        return

    for i in range(min(P) - 1, max(P) + 2):
        if i not in P:
            d = abs(i - X)
            if d == m:
                n = min(n, i)
            elif d < m:
                m = d
                n = i

    print(n)


def __starting_point():
    solve()


__starting_point()
