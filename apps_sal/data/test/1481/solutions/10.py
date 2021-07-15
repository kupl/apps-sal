__author__ = 'Natik'
n = int(input())
mas = [[100] * n for i in range(n)]
for i in range(0, n):
    mas[i] = input()
ot = 0
for i in range(0, n):
    for j in range(0, n):
        klo = 0
        if j+1 < n:
            if mas[i][j+1] == 'o':
                klo += 1
        if i+1 < n:
            if mas[i+1][j] == 'o':
                klo += 1
        if i-1 >= 0:
            if mas[i-1][j] == 'o':
                klo += 1
        if j-1 >= 0:
            if mas[i][j-1] == 'o':
                klo += 1
        if klo % 2 == 1:
            ot = 1
if ot == 0:
    print('YES')
else:
    print('NO')
