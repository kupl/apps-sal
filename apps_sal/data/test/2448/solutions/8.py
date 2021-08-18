import sys
import os
import math
import itertools
import functools
from fractions import Fraction
import array
3


def main():
    T = read_int()
    for _ in range(T):
        N = read_int()
        A, B, C = read_ints()
        S = inp()
        ans = solve(N, A, B, C, S)
        if not ans:
            print('NO')
        else:
            print('YES')
            print(ans)


def solve(N, A, B, C, S):
    sol = [None] * N
    wins = 0
    for i in range(N):
        if S[i] == 'S' and A > 0:
            sol[i] = 'R'
            A -= 1
            wins += 1
        if S[i] == 'R' and B > 0:
            sol[i] = 'P'
            B -= 1
            wins += 1
        if S[i] == 'P' and C > 0:
            sol[i] = 'S'
            C -= 1
            wins += 1

    if wins < (N + 1) // 2:
        return None

    for i in range(N):
        if sol[i] is None:
            if A > 0:
                sol[i] = 'R'
                A -= 1
            elif B > 0:
                sol[i] = 'P'
                B -= 1
            else:
                sol[i] = 'S'
                C -= 1

    return ''.join(sol)


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
