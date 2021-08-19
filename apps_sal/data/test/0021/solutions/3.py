from sys import *


def inp():
    return stdin.readline()


def main():
    n = int(inp())
    (a, b) = (0, 0)
    l = [int(i) for i in inp().split()]
    for i in range(len(l)):
        if l[i] == 1:
            a = i
        if l[i] == n:
            b = i
    if a > b:
        (a, b) = (b, a)
    ans = max(n - 1 - a, b)
    print(ans)


def __starting_point():
    main()


__starting_point()
