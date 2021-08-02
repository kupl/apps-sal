#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
snacks = list(map(int, input().split()))
status = [False] * (n + 1)

biggest = n
for day, snack in enumerate(snacks):
    status[snack] = True
    ret = ''
    if biggest == snack:
        biggest -= 1
        while status[biggest] and biggest >= 1:
            biggest -= 1
        ret_list = list(range(biggest + 1, snack + 1))
        ret = ' '.join(map(str, reversed(ret_list)))
    print(ret)
