#!/usr/bin/env python3
import sys
from itertools import combinations_with_replacement, product
def input(): return sys.stdin.readline().rstrip()


def main():
    D, G = list(map(int, input().split()))
    problem = []
    for i in range(1, D + 1):
        p, c = list(map(int, input().split()))
        problem.append([i, p, c])
    ans = 10000000
    for bit in list(product([0, 1], repeat=D)):
        pnum = 0
        nokori = G
        notcomp = []
        for i in range(D):
            if bit[i] == 1:
                pnum += problem[i][1]
                nokori -= problem[i][2] + problem[i][1] * problem[i][0] * 100
            else:
                notcomp.append(problem[i])
        while nokori > 0 and notcomp:
            score, p, c = notcomp.pop()
            if score * (p - 1) * 100 <= nokori:
                nokori -= score * (p - 1) * 100
                pnum += p - 1
            else:
                tmp = score * 100
                pnum += (nokori + tmp - 1) // tmp
                nokori = 0
        if nokori <= 0:
            ans = min(ans, pnum)
    print(ans)


def __starting_point():
    main()


__starting_point()
