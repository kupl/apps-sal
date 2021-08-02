import math
import sys


def main():
    l = input()
    rr = 0
    br = 0
    gr = 0
    yr = 0
    for i in range(len(l)):
        if l[i] == 'R':
            rr = i % 4
        if l[i] == 'B':
            br = i % 4
        if l[i] == 'Y':
            yr = i % 4
        if l[i] == 'G':
            gr = i % 4
    rk = 0
    bk = 0
    gk = 0
    yk = 0
    for i in range(len(l)):
        if l[i] == "!":
            if i % 4 == rr:
                rk += 1
            if i % 4 == br:
                bk += 1
            if i % 4 == yr:
                yk += 1
            if i % 4 == gr:
                gk += 1
    print(rk, bk, yk, gk)


def __starting_point():
    main()


__starting_point()
