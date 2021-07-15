#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:25:50 2019

@author: pawangoyal
"""
input_1=input()
input_1=input_1.split()
n = int(input_1[0])
k = int(input_1[1])
x = int(input_1[2])

a=input()
a=a.split()
a=[int(x) for x in a]
maximum=0
prefix=[]
suffix=[]

prefix_or = 0
suffix_or = 0

for i in range(n):
    prefix_or = prefix_or|a[i]
    prefix.append(prefix_or)

for i in range(n-1,-1,-1):
    suffix_or = suffix_or|a[i]
    suffix.append(suffix_or)
 
or_bit=0

if n ==1 :
    or_bit=a[0]*(x**k)
else:
    for i in range(n):
        if i == 0:
            or_bit=max(or_bit,(a[0]*(x**k)|suffix[n-2]))
        elif i == (n-1):
            or_bit=max(or_bit,(a[n-1]*(x**k)|prefix[n-2]))
        else:
            or_bit=max(or_bit,(a[i]*(x**k)|prefix[i-1]|suffix[n-2-i]))
   
    
print(or_bit)


