#!/usr/bin/env python3
from collections import defaultdict


def main():
    n = int(input())
    a = [int(ai) for ai in input().split()]

    pref_sums = [0] * (n + 1)
    for i, ai in enumerate(a):
        pref_sums[i + 1] = pref_sums[i] + ai

    block_sums = defaultdict(list)
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            block_sums[pref_sums[j] - pref_sums[i - 1]].append((i, j))

    ans = []
    for A in list(block_sums.values()):
        res, k = [A[0]], 0
        for i in range(1, len(A)):
            if A[i][0] > A[k][1]:
                res.append(A[i])
                k = i

        if len(res) > len(ans):
            ans = res

    print(len(ans))
    print('\n'.join(['%d %d' % s for s in ans]))


def __starting_point():
    main()


__starting_point()
