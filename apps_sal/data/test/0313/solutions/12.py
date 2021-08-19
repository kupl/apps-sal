#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

N = int(input())
S = input()
S = S.replace(" ", "")
S = S.strip("0")

ret = 0
for seg in re.split("00+", S):
    ret += len(seg)

print(ret)
