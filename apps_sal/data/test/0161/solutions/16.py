import sys
import math
3


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(X):
    nops = 0
    ns = []

    while True:
        s = '{:b}'.format(X)
        ls = len(s)
        zerop = s.find('0')
        if X == 0 or zerop == -1:
            break

        n = ls - zerop
        ns.append(n)
        nops += 1
        X ^= (1 << n) - 1

        s = '{:b}'.format(X)
        zerop = s.find('0')
        if X == 0 or zerop == -1:
            break

        X += 1
        nops += 1

    return nops, ns


def main():
    X = int(inp())
    nops, ns = solve(X)
    print(nops)
    if ns:
        print(*ns)


def __starting_point():
    main()


__starting_point()
