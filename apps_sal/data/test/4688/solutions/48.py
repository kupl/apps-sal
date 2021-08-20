def resolve():
    (n, k) = list(map(int, input().split()))
    print(k * (k - 1) ** (n - 1))


def __starting_point():
    resolve()


__starting_point()
