# coding: utf-8
from math import sqrt


def main():
    X = int(input())

    for i in range(X, 100004):
        tmp = int(sqrt(i))
        flg = False
        for j in range(2, tmp + 1):
            if (i % j == 0):
                flg = True
                break
        if flg == False:
            ans = i
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
