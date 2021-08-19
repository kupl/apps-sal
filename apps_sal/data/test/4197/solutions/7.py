"""
Created on Wed Sep  9 02:37:37 2020

@author: liang
"""
'\nkey = lambda x:x[1]\n'
N = int(input())
A = [int(i) for i in input().split()]
B = [(i + 1, A[i]) for i in range(N)]
B.sort(key=lambda x: x[1])
res = [str(b[0]) for b in B]
print(' '.join(res))
