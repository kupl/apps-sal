#!/usr/bin/env python3

try:
    while True:
        n, k = list(map(int, input().split()))
        print((n + k) // k * k)

except EOFError:
    pass
