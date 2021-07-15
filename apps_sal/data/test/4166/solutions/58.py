# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:36:58 2020

@author: liang
"""
"""
全探索
"""
N, M = map(int, input().split())

test = list()
for _ in range(M):
    s,c =  map(int,input().split()) 
    test.append((s,c))

#print(test)
tmp = [0]*3
for i in range(10**N):
    tmp[0] = i//100
    tmp[1] = i//10%10
    tmp[2] = i%10
    #print(tmp)
    for tup in test:
        s, c = tup[0], tup[1]
        if tmp[(3-N)+s-1] != c:
            break
    else:
        #最上位の桁が0でないか
        if tmp[-N] == 0 and N != 1:
            continue
        print(i)
        break
else:
    print(-1)
