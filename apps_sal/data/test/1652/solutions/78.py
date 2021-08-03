#!/usr/bin/env python3
import sys
INF = float("inf")

sys.setrecursionlimit(10**5)


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


template = ["dream", "dreamer", "erase", "eraser"]


def dfs(s, i):
    if i == len(s):
        return True
    for t in template:
        if s[i:].startswith(t):
            if dfs(s, i + len(t)):
                return True
    return False


def solve(S: str):
    if dfs(S, 0):
        yes()
    else:
        no()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


def __starting_point():
    main()


__starting_point()
