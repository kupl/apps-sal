def iroha():
    x, a, b = list(map(int, input().split()))

    if a - b >= 0:
        print("delicious")
    elif x + a - b >= 0:
        print("safe")
    else:
        print("dangerous")


def __starting_point():
    iroha()


__starting_point()
