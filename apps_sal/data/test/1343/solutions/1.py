#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N,M,K = list(map(int,input().split()))

ftcs = []
for m in range(M):
    f,t,c=list(map(int,input().split()))
    ftcs.append((f,t,c))
if K != 0:
    storages = list(map(int,input().split()))
else:
    storages = []
storages_s = set(storages)

mn = 1e20
for f,t,c in ftcs:
    if (f in storages_s and t not in storages_s) or \
       (t in storages_s and f not in storages_s):
        mn = min(mn, c)
if mn == 1e20:
    print(-1)
else:
    print(mn)

    
        

    

