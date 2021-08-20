def iroha():
    li = list(map(int, input().split()))
    li.sort()
    merge = li[0] + li[1]
    if merge == li[2]:
        print('Yes')
    else:
        print('No')


def __starting_point():
    iroha()


__starting_point()
