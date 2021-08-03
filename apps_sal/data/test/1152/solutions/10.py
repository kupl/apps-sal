n, m = map(int, input().split())
mata = [None] * n
for i in range(n):
    mata[i] = list(map(int, input().split()))
matb = [None] * n
for i in range(n):
    matb[i] = list(map(int, input().split()))
for i in range(n - 1):
    for j in range(m - 1):
        if(mata[i][j] == 0):
            mata[i][j] = 1
            mata[i + 1][j] ^= 1
            mata[i][j + 1] ^= 1
            mata[i + 1][j + 1] ^= 1
        if(matb[i][j] == 0):
            matb[i][j] = 1
            matb[i + 1][j] ^= 1
            matb[i][j + 1] ^= 1
            matb[i + 1][j + 1] ^= 1
if(mata == matb):
    print("Yes")
else:
    print("No")
