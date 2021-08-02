#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int):
    m = [0] * 100
    for n in range(N + 1):
        s = str(n)
        h = int(s[0])
        l = int(s[-1])
        if l != 0:
            m[h * 10 + l] += 1

    answer = 0
    for h in range(1, 10):
        for l in range(1, 10):
            answer += m[h * 10 + l] * m[l * 10 + h]
    return answer


def main():
    N = int(input())
    answer = solve(N)
    print(answer)


def __starting_point():
    main()


__starting_point()
