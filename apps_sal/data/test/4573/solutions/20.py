"""
Created on Tue Sep 22 14:57:09 2020

@author: liang
"""
N = int(input())
X = [int(x) for x in input().split()]
Y = X.copy()
Y.sort()
upper = Y[N // 2]
lower = Y[N // 2 - 1]
for i in range(N):
    if X[i] < upper:
        print(upper)
    else:
        print(lower)
