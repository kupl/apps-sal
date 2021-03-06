""" 
Author: Raj Singh
Date:   31.01.19"""
from sys import stdin, stdout


def inp():
    return stdin.readline()


def minp():
    return map(int, stdin.readline().rstrip().split())


def linp():
    return list(minp())


def main():
    n = int(inp())
    lst = linp()
    lst.sort()
    s = 0
    for i in range(int(n / 2)):
        s += (lst[n - i - 1] + lst[i]) ** 2
    print(s)


def __starting_point():
    main()


__starting_point()
