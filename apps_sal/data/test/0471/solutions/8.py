# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:53:13 2016

@author: Felicia
"""

inp1 = input()
inp11 = inp1.split(' ')
n = int(inp11[0])
a = int(inp11[1])

inp2 = input()
inp21 = inp2.split(' ')
x0 = []
for i in inp21:
    j=int(i)
    x0.append(j)

x = sorted(x0)

def f(x):
    if x>0:
        return x
    else:
        return 0
if n>1:
    len1 = 2*f(a-x[0])+f(x[n-2]-a)
    len2 = 2*f(x[n-2]-a)+f(a-x[0])
    len3 = 2*f(a-x[1])+f(x[n-1]-a)
    len4 = 2*f(x[n-1]-a)+f(a-x[1])
    
    print(min(len1,len2,len3,len4))
else:
    print(0)
