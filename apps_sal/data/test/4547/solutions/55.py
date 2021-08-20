def iroha():
    num = list(input())
    for i in num:
        if i == '9':
            print('Yes')
            return
    print('No')


def __starting_point():
    iroha()


__starting_point()
