def iroha():
    num = input()
    count = 0

    for i in num:
        if i == '1':
            count += 1

    print(count)


def __starting_point():
    iroha()


__starting_point()
