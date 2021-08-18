#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]

for target in range(2**9):
    mask = ~target
    all_ok = True
    for ai in a:
        ok = False
        for bi in b:
            if not (ai & bi) & mask:
                ok = True
                break
        if not ok:
            all_ok = False
            break
    if all_ok:
        print(target)
        return
