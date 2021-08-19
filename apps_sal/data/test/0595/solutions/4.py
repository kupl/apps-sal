#!/usr/bin/env python3

def is_leap(y):
    return bool(not y % 400 or (not y & 0x3 and y % 100))


try:
    while True:
        y = int(input())
        prev_leap = initial_leap = is_leap(y)
        m = 0
        while True:
            if prev_leap:
                m += 2
            else:
                m += 1
            m %= 7
            y += 1
            prev_leap = is_leap(y)
            if not m and prev_leap == initial_leap:
                print(y)
                break

except EOFError:
    pass
