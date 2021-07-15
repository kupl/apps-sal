import sys
n, m = list(map(int, input().split()))
gg = [input() for i in range(n)]
used = 0
fir = [-1, -1]
sec = [-1, -1]
for i in range(n):
    for j in range(m):
        if gg[i][j] == 'X':
            if not used:
                used = 1
                fir = [i, j]
            sec = [i, j]
for i in range(fir[0], sec[0] + 1):
    for j in range(fir[1], sec[1] + 1):
        if gg[i][j] == '.':
            print('NO')
            return
for i in range(n):
    for j in range(m):
        if fir[0] <= i <= sec[0] and fir[1] <= j <= sec[1]:
            continue
        if gg[i][j] == 'X':
            print('NO')
            return
print('YES')

