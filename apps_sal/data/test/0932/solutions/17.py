from math import *

n, m = input().split()
n, m = int(n), int(m)

b = [[int(i) for i in input().split()] for i in range(n)]
a = [[1] * m for i in range(n)]
c = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (b[i][j] == 0):
            for k in range(m):
                a[i][k] = 0
                
            for k in range(n):
                a[k][j] = 0
                
for i in range(n):
    for j in range(m):
        c[i][j] = 0
        
        for k in range(m):
            if (a[i][k] == 1):
                c[i][j] = 1
                break
                
        if (c[i][j] == 1):
            continue
            
        for k in range(n):
            if (a[k][j] == 1):
                c[i][j] = 1
                break
                
bad = False
                
for i in range(n):
    for j in range(m):
        if (c[i][j] != b[i][j]):
            bad = True
            print('NO')
            break
            
    if (bad):
        break

if (not bad):
    print('YES')
    
    for i in range(n):
        for j in range(m):
            print(a[i][j], end = ' ')
            
        print()
