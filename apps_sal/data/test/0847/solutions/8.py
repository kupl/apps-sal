from math import *


def main():

    n, x = map(int, input().split())
    A = abs(sum(list(map(int, input().split()))))
    if A == 0:
        print(0)
        return
    l = 0
    r = 10**8
    while r - l > 1:
        m = (l + r) // 2
        if A - m * x > 0:
            l = m
        else:
            r = m
    print(r)


main()
