#!/usr/bin/env python3

import collections

def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a = collections.Counter(a)
        a = [a[i] for i in a]
        a = sorted(a)[::-1]
        bins = a[0] - 1
        for i in range(1, len(a)):
            if a[i] == a[0]:
                a[i] -= 1
        rem = sum(a[1:])
        print(rem // bins)

def __starting_point():
    main()

__starting_point()
