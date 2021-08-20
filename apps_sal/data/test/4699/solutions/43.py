import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


def __starting_point():
    nk = list(map(int, input().split()))
    x = nk[1]
    dList = list(map(int, input().split()))
    f = 0
    n = nk[0]
    while f == 0:
        nList = [int(c) for c in str(n)]
        b = 1
        for i in nList:
            for j in dList:
                if i == j:
                    b = 0
                    break
        if b == 1:
            break
        else:
            n += 1
    print('{}'.format(n))


__starting_point()
