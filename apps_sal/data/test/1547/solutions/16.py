mx = []
ops = []
nx = list(map(int, input().split()))
n = nx[0]
m = nx[1]
k = nx[2]
flagn = [(-1, -1, i) for i in range(0, n)]
flagm = [(-1, -1, i) for i in range(0, m)]
for i in range(0, n):
    mx.append([0] * m)
for i in range(0, k):
    temp = (list(map(int, input().split())))
    if temp[0] == 1:
        flagn[temp[1] - 1] = (i, temp[2], temp[1] - 1)
    else:
        flagm[temp[1] - 1] = (i, temp[2], temp[1] - 1)
flagn.sort(key=lambda x: x[0])
flagm.sort(key=lambda x: x[0])
pntn = 0
pntm = 0
for i in range(0, n + m):
    if ((pntn < n) & (pntm < m)):
        if flagn[pntn][0] <= flagm[pntm][0]:
            if (flagn[pntn][0] != -1):
                for j in range(0, m):
                    mx[flagn[pntn][2]][j] = flagn[pntn][1]
            i += 1
            pntn += 1
        else:
            if flagm[pntm][0] != -1:
                for j in range(0, n):
                    mx[j][flagm[pntm][2]] = flagm[pntm][1]
            i += 1
            pntm += 1
    else:
        if (pntn < n):
            if (flagn[pntn][0] != -1):
                for j in range(0, m):
                    mx[flagn[pntn][2]][j] = flagn[pntn][1]
            i += 1
            pntn += 1
        if (pntm < m):
            if flagm[pntm][0] != -1:
                for j in range(0, n):
                    mx[j][flagm[pntm][2]] = flagm[pntm][1]
            i += 1
            pntm += 1
for i in range(0, n):
    for j in range(0, m):
        print(mx[i][j], end=' ')
    print()
