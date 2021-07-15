# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 18:46:09 2018

@author: Sand Boa
"""
import itertools

def __starting_point():
    n:int
    T:int
    n, T = list(map(int,input().split()))
    listi:list = []
    tsum:int = 0
    csum:int = 0
    k:int
    k = 1
    a:int
    b:int
    t:int
    ind:int
    for i in range(n):
        a,b = list(map(int,input().split()))
        listi.append((a,b,i))
    #print(listi)
    listi = sorted(listi, key=lambda x: x[1])
    #print(listi)
    time:list = [0] * (n + 1)
    count:list = [0] * (n + 1)
    for (a, t, ind) in listi:
        if k <= a:
            tsum += t
            time[a] += t
            if tsum > T:
                break
            count[a] += 1
            csum += 1
            if csum == k:
                csum -= count[k]
                tsum -= time[k]
                k += 1
    max_score:int = max(csum, k - 1)
    print (max_score,max_score,sep='\n')
    print(*list(itertools.islice((idx + 1 for (a, t, idx) in listi if a >= max_score),max_score)))


				    						    	 	  	 			 	
__starting_point()
