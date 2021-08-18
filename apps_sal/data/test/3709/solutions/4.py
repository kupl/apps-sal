"""
Created on Thu Oct  5 13:30:23 2017

@author: savit
"""

n, k = list(map(int, input().split()))
s = []
A = []
for i in range(16):
    A.append(False)
for i in range(n):
    s.append(input())
    s[i] = s[i].replace(' ', '')
    s[i] = s[i] + '0' * (4 - k)
    s[i] = int(s[i], 2)
    A[s[i]] = True
fl = False
if(A[0]):
    fl = True
if(A[1]):
    for i in range(2, 16, 2):
        if(A[i]):
            fl = True
if(A[2] and (A[4] or A[5] or A[8] or A[9] or A[12] or A[13] or A[1])):
    fl = True
if(A[4] and (A[8] or A[9] or A[10] or A[11] or A[3] or A[1] or A[2])):
    fl = True
if(A[8]):
    for i in range(8):
        if(A[i]):
            fl = True
if(A[3] and A[12]):
    fl = True
if(A[6] and A[9]):
    fl = True
if(A[5] and A[10]):
    fl = True
if(fl):
    print('YES')
else:
    print('NO')
