#!/usr/bin/env python3

try:
    while True:
        x1, y1 = list(map(int, input().split()))
        x2, y2 = list(map(int, input().split()))
        print(max(abs(x1 - x2), abs(y1 - y2)))

except EOFError:
    pass
