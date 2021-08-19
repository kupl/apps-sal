def iroha():
    (a, b, c) = list(map(int, input().split()))
    if a == b and b == c and (a == c):
        print(1)
    elif a != b and b != c and (a != c):
        print(3)
    else:
        print(2)


def __starting_point():
    iroha()


__starting_point()
