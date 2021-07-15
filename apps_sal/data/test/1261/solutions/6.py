3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N):
    ans = []

    end = N
    fac = 1

    while end >= 1:
        if end == 1:
            ans.append(fac)
            end = 0
            break

        if end == 2:
            ans.append(fac)
            ans.append(fac * 2)
            end = 0
            break

        if end == 3:
            ans.append(fac)
            ans.append(fac)
            ans.append(fac * 3)
            end = 0
            break

        ans.extend([fac] * ((end + 1) // 2))
        end //= 2
        fac *= 2

    return ans


def main():
    N = int(inp())
    print(*solve(N))


def __starting_point():
    main()

__starting_point()
