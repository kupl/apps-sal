"""
Created on Jan 28, 2015

@author: RedNextYear
"""
t = [list(map(int, input().split())) for i in range(3)]
p = [[1] * 5 for i in range(5)]
for i in range(3):
    for j in range(3):
        if t[i][j] % 2 == 1:
            p[i][j + 1] += 1
            p[i + 2][j + 1] += 1
            for v in range(j, j + 3):
                p[i + 1][v] += 1
for i in range(1, 4):
    print(''.join((str(p[i][j] % 2) for j in range(1, 4))))
