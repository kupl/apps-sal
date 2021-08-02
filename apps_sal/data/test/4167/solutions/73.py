def solve():
    n, k = list(map(int, input().split()))
    if k % 2 != 0:
        print(((n // k) ** 3))
    else:
        print(((n // k) ** 3 + ((n + k // 2) // k) ** 3))


def __starting_point():
    solve()


__starting_point()
