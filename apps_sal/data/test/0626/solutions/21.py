#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
C = list(map(int, input().split()))


def check(init):
    d = init
    done = [False for i in range(n)]
    cracked = 0
    changed = 0
    while cracked < n:
        if d == 0:
            for i in range(n):
                if not done[i] and C[i] <= cracked:
                    done[i] = True
                    cracked += 1
        else:
            for i in range(n)[::-1]:
                if not done[i] and C[i] <= cracked:
                    done[i] = True
                    cracked += 1
        d = d ^ 1
        if cracked < n:
            changed += 1
    return changed


print(check(0))
