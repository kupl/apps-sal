#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations

n = int(input())
lines = [input() for i in range(0,n)]
ans = 0

for a,b in combinations([chr(i) for i in range(ord('a'),ord('z')+1)], 2):
    hoge = 0
    for l in lines:
        sets = set(l)
        if len(sets) > 2 or (a not in sets and b not in sets): continue
        if len(sets) == 2 and not (a in sets and b in sets): continue
        hoge += len(l)
    ans = max(ans, hoge)
print(ans)
        
            

