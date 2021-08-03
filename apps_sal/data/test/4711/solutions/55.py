def iroha():
    lists = list(map(int, input().split()))
    lists.sort()
    print((lists[0] + lists[1]))


def __starting_point():
    iroha()


__starting_point()
