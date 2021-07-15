#!/usr/bin/env python3

try:
    while True:
        a, b, c = list(map(int, input().split()))
        x, y, z = list(map(int, input().split()))
        a -= x
        b -= y
        c -= z
        if sum(t >> 1 for t in (a, b, c) if t > 0) >= sum(-t for t in (a, b, c) if t < 0):
            print("Yes")
        else:
            print("No")

except EOFError:
    pass

