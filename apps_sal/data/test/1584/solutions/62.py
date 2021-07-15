# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:39:55 2020

@author: liang
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:56:06 2020

@author: liang
"""

N = int(input())
L = [int(x) for x in input().split()]

from bisect import bisect_left

L.sort()
ans = 0
#print(L)
for i in range(N-2):
    #print("1:",i)
    #p = i+2
    #以下O(2N)　定数倍が遅い
    for j in range(i+1,N-1):
        #print("2",i,j)
        t = L[i] + L[j]
        #while p < N and L[p] < L[i] + L[j] :
        #    p += 1
        p = bisect_left(L,t)
            #print("up")
        #print(p)
        #ans += len(L[j+1:p])
        ans += max(0, p - j -1)
print(ans)
