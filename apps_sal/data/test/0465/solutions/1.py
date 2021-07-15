#     Educational Codeforces Round 45 (Rated for Div. 2)
import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    

 
            
    
n,a,b = getIntList()
a0 = a
b0 = b
if a0>b0:
    a0,b0 = b,a
if n==2 and (a0,b0) == (1,1):
    print('NO')
    return
if n==3 and (a0,b0) == (1,1):
    print('NO')
    return    
if a>1 and b>1:
    print('NO')
    return

mat = [['0' for y in range(n)]for x in range(n)]
mat1 = [['1' for y in range(n)]for x in range(n)]
if b==1:
    for x in range(n-a):
        mat[x][x+1] = '1'
        mat[x+1][x] = '1'
else:
    mat = mat1
    for x in range(n):
        mat[x][x] = '0'
    for x in range(n-b):
        mat[x][x+1] = '0'
        mat[x+1][x] = '0'

print('YES')
for x in range(n):
    print(''.join(mat[x]))

