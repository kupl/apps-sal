import sys
import math
3
DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(S):
    vv = 0
    o = 0
    cnt = 0
    N = len(S)
    for i in range(N):
        if S[i:i + 2] == 'vv':
            cnt += o
            vv += 1
        elif S[i] == 'o':
            o += vv
    return cnt


def main():
    S = inp()
    print(solve(S))


def __starting_point():
    main()


__starting_point()
