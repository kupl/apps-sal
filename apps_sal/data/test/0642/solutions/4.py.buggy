# /usr/bin/env python

import sys

n, m = tuple(int(x) for x in input().split(" ") if len(x) > 0)
if m == 0:
    print("YES")
    return

d = [int(x) for x in input().split(" ") if len(x) > 0]


d.sort()


def solve():
    if d[0] == 1:
        return "NO"

    if d[-1] == n:
        return "NO"

    lc = 0
    for x in range(m - 1):
        i = d[x]
        j = d[x + 1]
        if i == j - 1:
            lc += 1
            if lc > 1:
                return "NO"
        else:
            lc = 0

    return "YES"


print(solve())
