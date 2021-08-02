def iroha():
    a, b = list(map(int, input().split()))

    ans = a + b

    print((ans if ans < 10 else "error"))


def __starting_point():
    iroha()


__starting_point()
