#!/usr/bin/env python3
import sys

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

q = int(input())

order = [0]*(2*10**5+1)
lm_order = 0
rm_order = 0

not_init = 1
for i in range(q):
    cmd, id = sys.stdin.readline().split()
    id = int(id)
    if cmd == 'L':
        order[id] = lm_order - 1
        lm_order = lm_order - 1
        if not_init:
            rm_order = lm_order
            not_init = 0
    elif cmd == 'R':
        order[id] = rm_order + 1
        rm_order = rm_order + 1
        if not_init:
            lm_order = rm_order
            not_init = 0
    else:
        print(min(order[id]- lm_order, rm_order - order[id]))


