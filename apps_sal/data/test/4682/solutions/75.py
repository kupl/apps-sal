def iroha():
    (a, b, c) = [int(input()) for i in range(3)]
    num = (a + b) * c / 2
    result = int(num)
    print(result)


def __starting_point():
    iroha()


__starting_point()
