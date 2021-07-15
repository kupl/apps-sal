#!/usr/bin/env python3

def gcd(x, y):
    if y == 0 or x == 0:
        return max(x, y)
    t = x % y
    while t != 0:
        x = y
        y = t;
        t = x % y
    return y

def main():
    readData = lambda : list(map(int, input().split()))
    n = int(input())
    X = list(readData())
    d = 0
    for x in X:
        d = gcd(d, x)
    print(d * len(X))

def __starting_point():
    main()

__starting_point()
