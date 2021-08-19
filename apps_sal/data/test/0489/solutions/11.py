# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:41:20 2017

@author: prophet
"""

n = input()
a = input().split()
a = [int(x) for x in a]
a.sort()
y = a[2]
arr = [x for x in a if x == y]
ns = len(arr)
if(a[0] == y):
    print(int(ns * (ns - 1) * (ns - 2) / 6))
elif(a[1] == y):
    print(int(ns * (ns - 1) / 2))
else:
    print(ns)
