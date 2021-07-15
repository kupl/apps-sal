# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:37:12 2020

@author: liang
"""
import math
X = int(input())
N = int(math.sqrt(X))
lis = list(range(2,N+1))
#print(N)
#print(lis)
ans = X 

while True:
    if all(ans%i != 0 for i in lis):
        print(ans)
        break
    #print(ans)
    ans += 1
