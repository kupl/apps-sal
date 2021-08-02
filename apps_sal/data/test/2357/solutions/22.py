from sys import stdin, stdout

import collections


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = [int(x) for x in input().split(' ')]
        prev_idx = {}
        min_dist = float('inf')
        for i, v in enumerate(a):
            if v in prev_idx:
                min_dist = min(min_dist, i - prev_idx[v] + 1)
            prev_idx[v] = i
        print(-1 if min_dist == float('inf') else min_dist)


def __starting_point():
    main()


__starting_point()
