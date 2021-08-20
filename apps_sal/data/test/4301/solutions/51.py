"""
Created on Thu Sep 10 00:13:41 2020

@author: liang
"""
N = int(input())
A = [int(input()) for i in range(N)]
B = A.copy()
B.sort()
for i in range(N):
    if A[i] == B[-1]:
        print(B[-2])
    else:
        print(B[-1])
