import os
import sys


def solve(arr):
    items = sorted(set(arr))
    min_max = [(float("inf"), float("-inf"))] * len(items)
    item_to_idx = {k: idx for idx, k in enumerate(items)}
    for idx, a in enumerate(arr):
        m, M = min_max[item_to_idx[a]]
        min_max[item_to_idx[a]] = (min(idx, m), max(idx, M))

    best = 1
    current = 1
    for i in range(1, len(items)):
        _, prev_M = min_max[i - 1]
        m, _ = min_max[i]
        if prev_M <= m:
            current += 1
        else:
            current = 1

        best = max(best, current)

    return len(items) - best


def pp(input):
    T = int(input())
    for t in range(T):
        input()
        arr = list(map(int, input().strip().split()))
        print(solve(arr))


if "paalto" in os.getcwd():
    from string_source import string_source, codeforces_parse

    pp(
        string_source(
            """3
7
3 1 6 6 3 1 1
8
1 1 4 4 4 7 8 8
7
4 2 5 2 6 2 7"""
        )
    )
else:
    pp(sys.stdin.readline)

