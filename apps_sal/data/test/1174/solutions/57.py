# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:35:58 2020

@author: liang
"""

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort(reverse=True)
#print(A)
count = 0
while count != M:
    A[0] //= 2
    count += 1
    tmp = A[0]
    for i in range(1,N):
        if count == M:
            break
        if A[i] > tmp:
            A[i] //= 2
            count += 1
        ##   break
    A.sort(reverse=True)
ans = sum(A)
#print(A)
print(ans)
