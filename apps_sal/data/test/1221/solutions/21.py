# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:39:42 2018

@author: Paras Sharma
"""

n, m = list(map(int, input().split()))
nl = []
ml = []
nl = list(map(int, input().split()))
ml = list(map(int, input().split()))
nl.sort()
ml.sort()
a = nl[0] * ml[-1]
b = nl[-1] * ml[0]
c = nl[-1] * ml[-1]
d = nl[0] * ml[0]
curr = [a, b, c, d]
if max(curr) == a or max(curr) == d:
    nl.pop(0)
else:
    nl.pop(-1)

a = nl[0] * ml[-1]
b = nl[-1] * ml[0]
c = nl[-1] * ml[-1]
d = nl[0] * ml[0]
curr = [a, b, c, d]
print(max(curr))
