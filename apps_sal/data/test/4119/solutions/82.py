# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:32:27 2020

@author: liang
"""
"""
配列のスライス
X[0:-(N-1)]などで切ると、N=1の時にバグるので注意
X[0:len(X) - (N-1)]のように要素数-後ろから数えたindexとする

"""
N, M = map(int, input().split())
X = [int(x) for x in input().split()]

def solve():
    if N >= M :
        return 0
    X.sort()
    d = [X[i+1] - X[i] for i in range(M-1)]
    d.sort()
    #print(X)
    #print(d)
    return sum(d[0:M-N])
print(solve())
