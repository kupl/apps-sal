def solve():
    N = int(input())
    T = input()

    if T == '1':
        print((10**10 * 2))
        return

    splited = T.split('0')
    if len(splited[0]) > 2 or len(splited[-1]) > 2:
        print('0')
        return

    for i in range(1, len(splited) - 1):
        if len(splited[i]) != 2:
            print('0')
            return

    if len(splited) - 1 > 10**10:
        print('0')
        return

    if T[-1] == '0':
        print((10**10 - (len(splited) - 1) + 1))

    else:
        print((10**10 - (len(splited) - 1)))


def __starting_point():
    solve()


__starting_point()
