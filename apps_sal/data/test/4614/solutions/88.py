def iroha():
    (a, b, c) = list(map(int, input().split()))
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)


def __starting_point():
    iroha()


__starting_point()
