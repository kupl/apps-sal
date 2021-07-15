#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 21:01:01 2018

@st0rmbring3r
"""
# l = [int(x) for x in input().split()]

d2 = {'Power':'purple','Time':'green','Space': 'blue','Soul': 'orange','Reality': 'red','Mind': 'yellow'}
d1 = {d2[x]:x for x in d2}
# color: power
s = set(y for y in d1)

for _ in range(int(input())):
    s.remove(input())

print(len(s))
for x in s:
    print(d1[x])
