def iroha():
    a, b, c = list(map(int, input().split()))

    if a <= c and b >= c:
        print("Yes")
    else:
        print("No")


def __starting_point():
    iroha()


__starting_point()
