m, n = list(map(int, input().split()))
R = ['.'] * m
nR = [[0] * n for i in range(m)]

for i in range(m):
    A = list(input())
    # A.replace('.','0')
    R[i] = A[:]

for i in range(m):
    for j in range(n):
        if R[i][j] == '*':
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if ii == 0 and jj == 0:
                        continue
                    if 0 <= i + ii < m and 0 <= j + jj < n:
                        nR[i + ii][j + jj] += 1
# print(nR)
v = 1
for i in range(m):
    for j in range(n):
        if R[i][j] == '*':
            continue
        if R[i][j] == '.':
            if nR[i][j] != 0:
                v = 0
            continue
        if int(R[i][j]) != nR[i][j]:
            v = 0


if v == 1:
    print('YES')
else:
    print('NO')
