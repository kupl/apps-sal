# input
K = list(map(int, input().split()))
K.sort()


def solve():
    m = min(K)

    if m == 1:
        print('YES')
        return
    elif m >= 3:
        if K == [3, 3, 3]:
            print('YES')
            return
        else:
            print('NO')
            return
    else:  # m=2
        if K[1] == 2:
            print('YES')
            return
        elif K == [2, 4, 4]:
            print('YES')
            return
        else:
            print('NO')
            return


def __starting_point():
    solve()


__starting_point()
