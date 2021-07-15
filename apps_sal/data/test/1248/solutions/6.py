#!/usr/bin/env python3

try:
    while True:
        a, b, c = list(map(int, input().split()))
        if a > b:
            a, b = b, a
        d = min(a + b, c)
        print(a + d + min(b, a + d))
except EOFError:
    pass

