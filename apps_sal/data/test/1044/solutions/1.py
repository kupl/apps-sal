#!/usr/bin/env python3

try:
    while True:
        n = int(input())
        prev = 0
        for x in map(int, input().split()):
            prev = (prev + x - 1) & 0x1
            print("21"[prev])

except EOFError:
    pass
