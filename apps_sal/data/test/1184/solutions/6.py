# -*- coding: utf-8 -*-
import sys
f = sys.stdin
St = f.readline().strip()

letters = {}
for s in St:
    if s not in '{, }':
        if s not in letters:
            letters[s] = 1

print(len(letters))
