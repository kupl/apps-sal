#!/usr/bin/env python3

def main():
    def readData(): return list(map(int, input().split()))
    n, c = readData()
    X = list(readData())
    ret = 0
    for i in range(n - 1):
        ret = max(ret, X[i] - X[i + 1] - c)
    print(ret)


def __starting_point():
    main()


__starting_point()
