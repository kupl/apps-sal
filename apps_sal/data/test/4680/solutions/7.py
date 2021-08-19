import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


def __starting_point():
    aList = list(map(int, input().split()))
    x = 5
    c5 = 0
    c7 = 0
    for a in aList:
        if a == 5:
            c5 += 1
        elif a == 7:
            c7 += 1
    if c5 == 2 and c7 == 1:
        print('YES')
    else:
        print('NO')


__starting_point()
