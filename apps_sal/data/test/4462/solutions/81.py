"""
Created on Sun Sep 27 02:20:18 2020

@author: liang
"""
N = int(input())
A = [int(x) for x in input().split()]
c0 = 0
c4 = 0
for a in A:
    if a % 2 == 1:
        c0 += 1
    elif a % 4 == 0:
        c4 += 1
if c0 <= c4:
    print('Yes')
elif c0 + c4 == N and c0 == c4 + 1:
    print('Yes')
else:
    print('No')
