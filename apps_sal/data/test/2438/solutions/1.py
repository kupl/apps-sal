from sys import *
from heapq import *
from lib2to3.pgen2.token import MINUS


n = int(input())

S = input()

minus = n
curA = 0
curB = 0
for s in S:
    if s == 'A':
        if curB != 0:
            minus += curB
            curB = 0
            curA = 1
        else:
            curA += 1
    
    else:
        if curA != 0:
            minus += curA
            curA = 0
            curB = 1
        else:
            curB += 1
curA, curB = 0, 0
for i in range(n - 1, -1, -1):
    s = S[i]
    if s == 'A':
        if curB > 1:
            
            minus += curB - 1
            curB = 0
            curA = 1
        elif curB == 1:
            curB = 0
            curA = 1
        else:
            curA += 1
    else:
        if curA > 1:
            minus += curA - 1
            curA = 0
            curB = 1
        elif curA == 1:
            curA = 0
            curB = 1
        else:
            curB += 1


print(n *(n + 1) // 2 - minus)
'''
6
ABABAB
''' 
