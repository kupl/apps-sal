def iroha():
    n, a, b = list(map(int, input().split()))
    print((b if b <= a * n else a * n))


def __starting_point():
    iroha()


__starting_point()
