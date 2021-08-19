"""
Created on Tue Sep 22 04:07:05 2020

@author: liang
"""
C = [[int(x) for x in input().split()] for _ in range(3)]
A = [0] * 3
B = [0] * 3
ans = False
for a1 in range(C[0][0] + 1):
    tmp = True
    b1 = C[0][0] - a1
    b2 = C[0][1] - a1
    b3 = C[0][2] - a1
    a2 = C[1][0] - b1
    a3 = C[2][0] - b1
    if C[1][1] != a2 + b2:
        tmp = False
    if C[1][2] != a2 + b3:
        tmp = False
    if C[2][1] != a3 + b2:
        tmp = False
    if C[2][2] != a3 + b3:
        tmp = False
    if tmp == True:
        ans = True
if ans:
    print('Yes')
else:
    print('No')
