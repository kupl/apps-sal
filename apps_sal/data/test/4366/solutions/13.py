def iroha():
    (a, b) = list(map(int, input().split()))
    num = a + b
    if num >= 24:
        new_num = num % 24
        print(new_num)
    else:
        print(num)


def __starting_point():
    iroha()


__starting_point()
