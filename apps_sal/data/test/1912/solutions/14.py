#!/usr/bin/env python3
import sys
input = sys.stdin.readline


def is_ok(r, g, b, w):
    odd_cnt = 0
    if r % 2 == 1:
        odd_cnt += 1
    if g % 2 == 1:
        odd_cnt += 1
    if b % 2 == 1:
        odd_cnt += 1
    if w % 2 == 1:
        odd_cnt += 1
    if odd_cnt <= 1:
        return True
    else:
        return False


t = int(input())
for _ in range(t):
    r, g, b, w = map(int, input().split())
    if is_ok(r, g, b, w):
        print("Yes")
        continue
    ok = False
    for _ in range(4):
        if r > 0 and g > 0 and b > 0:
            r -= 1
            g -= 1
            b -= 1
            w += 1
            ok = is_ok(r, g, b, w)
        if ok:
            break
    if ok:
        print("Yes")
    else:
        print("No")
