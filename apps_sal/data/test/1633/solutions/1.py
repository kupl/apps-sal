import sys
import math

n, m, k = map(int, input().split())
field = []

for i in range(n + 2):
    field.append([])
    for j in range(m + 2):
        field[i].append(False)

for ind in range(k):
    i, j = map(int, input().split())
    field[i][j] = True
    for ii in (-1, 1):
        for jj in (-1, 1):
            if field[i + ii][j] and field[i][j + jj] and field[i + ii][j + jj]:
                print(ind + 1)
                return
                
print(0)
