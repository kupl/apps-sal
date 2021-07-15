import io
import os

from collections import Counter, defaultdict, deque
import sys

sys.setrecursionlimit(10 ** 5)


MOD = 10 ** 9 + 7


def solveBrute(N, AA, AB, BA, BB):

    possible = set()

    cache = set()

    def f(s):
        if s in cache:
            return
        cache.add(s)
        if len(s) == N:
            possible.add(s)
            return
        for i in range(len(s) - 1):
            pair = s[i : i + 2]
            if pair == "AA":
                f(s[: i + 1] + AA + s[i + 1 :])
            elif pair == "AB":
                f(s[: i + 1] + AB + s[i + 1 :])
            elif pair == "BA":
                f(s[: i + 1] + BA + s[i + 1 :])
            elif pair == "BB":
                f(s[: i + 1] + BB + s[i + 1 :])

    f("AB")
    return len(possible) % MOD


def solve(N, AA, AB, BA, BB):
    if N == 2:
        return 1
    pattern = AA + AB + BA + BB

    if pattern in ["ABAA", "BABA", "BABB", "BBAA"]:
        return pow(2, N - 3, MOD)
    elif pattern in ["ABBA", "BAAA", "BAAB", "BBBA"]:
        fib = [0] * (N + 1)
        fib[0] = 1
        fib[1] = 1
        for i in range(2, N + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
        return fib[N - 2]
    else:
        return 1

if False:
    for mask in range(1 << 4):
        for N in range(2, 10):
            args = [(mask >> 3) & 1, (mask >> 2) & 1, (mask >> 1) & 1, (mask >> 0) & 1]
            args = ["AB"[x] for x in args]
            print((N, "".join(args), "\t", solveBrute(N, *args)))
            assert solveBrute(N, *args) == solve(N, *args)
        print()

def __starting_point():

    TC = 1
    for tc in range(1, TC + 1):
        N = int(input())
        AA = input()
        AB = input()
        BA = input()
        BB = input()
        ans = solve(N, AA, AB, BA, BB)
        print(ans)

__starting_point()
