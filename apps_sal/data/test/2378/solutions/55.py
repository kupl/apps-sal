#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int


def calc_fraction_mod(numerator, denominator):
    '''
        returns numerator / denominator (mod MOD)
    '''
    inv = pow(denominator, MOD - 2, MOD)
    return numerator * inv % MOD


def solve(N: int, A: "List[int]", B: "List[int]"):
    conns = [[] for _ in range(N)]
    for i in range(N - 1):
        conns[A[i] - 1].append(B[i] - 1)
        conns[B[i] - 1].append(A[i] - 1)

    pows = []
    for i in range(N + 1):
        pows.append(pow(2, i, MOD))

    num = [0]
    visited = [False] * N

    def dfs(idx):
        visited[idx] = True
        children = 0
        subs = []
        for c in conns[idx]:
            if visited[c]:
                continue
            sub = dfs(c)
            children += sub
            subs.append(sub)
        subs.append(N - children - 1)
        #tmp = pow(2, N - 1, MOD)
        tmp = pows[N - 1]
        tmp -= 1  # all white
        for sub in subs:
            #tmp -= pow(2, sub, MOD) - 1
            tmp -= pows[sub] - 1
        num[0] += tmp
        return children + 1
    dfs(0)

    #deno = pow(2, N, MOD)
    deno = pows[N]
    num = num[0]
    ret = calc_fraction_mod(num, deno)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


def __starting_point():
    main()


__starting_point()
