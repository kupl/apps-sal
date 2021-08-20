import sys
(n, m) = map(int, input().split())
a = [[i for i in list(input())] for j in range(n)]
b = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'X':
            nx = j
            ny = i
            b = 1
            break
    if b:
        break
b = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if a[i][j] == 'X':
            dx = j
            dy = i
            b = 1
            break
    if b:
        break
b = 0
for i in range(n):
    for j in range(m):
        if i >= ny and j >= nx and (i <= dy) and (j <= dx):
            if a[i][j] != 'X' and b == 0:
                print('NO')
                b = 1
        elif a[i][j] == 'X' and b == 0:
            print('NO')
            b = 1
if b == 0:
    print('YES')
