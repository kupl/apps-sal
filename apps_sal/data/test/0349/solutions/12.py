n, m = (int(i) for i in input().split())
L1 = [[int(j) for j in input().split()] for i in range(n)]
L2 = [[int(j) for j in input().split()] for i in range(n)]
for i in range(n):
    for j in range(m):
        if L1[i][j] > L2[i][j]:
            buf = L1[i][j]
            L1[i][j] = L2[i][j]
            L2[i][j] = buf

t = 1
for i in range(n):
    for j in range(m):
        if i > 0:
            if L1[i][j] <= L1[i - 1][j]:
                t = 0
            if L2[i][j] <= L2[i - 1][j]:
                t = 0
        if j > 0:
            if L1[i][j] <= L1[i][j - 1]:
                t = 0
            if L2[i][j] <= L2[i][j - 1]:
                t = 0
if not t:
    print('Impossible')
else:
    print('Possible')

