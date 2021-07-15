__author__ = 'Глеб'
import sys
n = int(input())
desk = [[0] * (n + 10) for j in range(n + 10)]
for i in range(n):
    str = input()
    for j in range(n):
        if str[j] == 'x':
            desk[i][j] = 0
        else:
            desk[i][j] = 1
for i in range(n):
    for j in range(n):
        if (desk[i][j + 1] + desk[i][j - 1] + desk[i + 1][j] + desk[i - 1][j]) % 2 != 0:
            print('NO')
            return
print('YES')
