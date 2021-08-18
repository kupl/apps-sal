a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
for i in range(3):
    for j in range(3):
        if (a[i][j] in b):
            a[i][j] = 0
tnp = 0
for i in range(3):
    if (sum(a[i]) == 0):
        tnp += 1
for i in range(3):
    if (a[0][i] + a[1][i] + a[2][i] == 0):
        tnp += 1
if (a[0][0] + a[1][1] + a[2][2] == 0):
    tnp += 1
if (a[0][2] + a[1][1] + a[2][0] == 0):
    tnp += 1
if (tnp > 0):
    print("Yes")
else:
    print("No")
