import math


def main():
    n = int(input())
    aList = list(map(int, input().split()))
    sumA = 1
    if aList.count(0) > 0:
        print((0))
        return
    for a in aList:
        sumA *= a
        if sumA > 10 ** 18:
            print((-1))
            return
    print(sumA)


def __starting_point():
    main()


__starting_point()
