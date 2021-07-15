#!/usr/bin/env python3
import sys
from itertools import chain, count

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    a_max = max(A)
    ans = 0
    for i in count(0):
        mask = 2**i
        if mask > a_max:
            return ans
        c0 = 0
        c1 = 0
        for a in A:
            if a & mask:
                c1 += 1
            else:
                c0 += 1
        mask = mask % MOD
        ans = (ans + mask*(c0 * c1)) % MOD 

def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, A)
    print(answer)

def __starting_point():
    main()

__starting_point()
