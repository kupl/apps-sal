#!/usr/bin/env python3

from collections import Counter

try:
    while True:
        n = int(input())
        a = sorted(map(int, input().split()))
        t = 1
        for x in a:
            t = min(t, x) + 1

        print(t)

except EOFError:
    pass

