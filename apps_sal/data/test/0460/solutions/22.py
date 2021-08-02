#!/usr/bin/env python
import sys


def eligible(score, position, thresh):
    if score < thresh:
        return False
    i = (score // 50) % 475
    for __ in range(25):
        i = (i * 96 + 42) % 475
        if position == 26 + i:
            return True
    return False


def main():
    p, x, y = list(map(int, sys.stdin.readline().split()))
    diff = 0
    for __ in range(475):
        if eligible(x + diff, p, y):
            print("0")
            return
        diff -= 50
    diff = 0
    for __ in range(475):
        if eligible(x + diff, p, y):
            succ = diff // 100
            unsucc = (diff // 50) % 2  # if 1, we need additional success
            print(str(succ + unsucc))
            return
        diff += 50


main()
