import math


def main():
    s = input()
    k = int(input())
    ns = len(s)
    if ns % k != 0:
        print('NO')
        return
    k = int(ns / k)
    while len(s) > 0:
        crt = s[:k]
        crt1 = crt[::-1]
        s = s[k:]
        if crt != crt1:
            print('NO')
            return
    print('YES')


def __starting_point():
    main()


__starting_point()
