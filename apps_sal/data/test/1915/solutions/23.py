import sys
f = sys.stdin
#f = open('H:\\Portable Python 3.2.5.1\\test_248B1.txt') 

n = int(f.readline().strip())

d = [[1]*n for it in range(n)]
for i in range(1,n):
    for j in range(1,n):
        d[i][j] = d[i-1][j] + d[i][j-1]


print(d[n-1][n-1])

