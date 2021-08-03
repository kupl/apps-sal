def main():
    MAX_ = 10 ** 6

    N = int(input())
    A = list(map(int, input().split()))

    mi = MAX_
    mii = -1

    ma = -MAX_
    mai = -1

    for i, x in enumerate(A):
        if mi > x:
            mi = x
            mii = i + 1
        if ma < x:
            ma = x
            mai = i + 1

    if mi >= 0:
        print((N - 1))
        for i in range(1, N):
            print((i, i + 1))
        return

    if ma <= 0:
        print((N - 1))
        for i in range(N - 1, 0, -1):
            print((i + 1, i))
        return

    print(((N - 1) * 2))
    if ma + mi >= 0:
        for i in range(1, N + 1):
            if i == mai:
                continue
            print((mai, i))
        for i in range(1, N):
            print((i, i + 1))
        return
    else:
        for i in range(1, N + 1):
            if i == mii:
                continue
            print((mii, i))
        for i in range(N - 1, 0, -1):
            print((i + 1, i))
        return


def __starting_point():
    main()


__starting_point()
