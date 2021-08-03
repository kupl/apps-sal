l = [[], [], [], [], [], []]
y = [[3, 3, 4, 4, 3, 3],
     [3, 3, 4, 4, 3, 3],
     [2, 2, 3, 3, 2, 2],
     [2, 2, 3, 3, 2, 2],
     [1, 1, 2, 2, 1, 1],
     [1, 1, 2, 2, 1, 1]]
for i in range(6):
    s = input()
    for j in s:
        if (j != '-'):
            l[i].append(j)
maxm = 0
maxi = 0
maxj = 0
for i in range(6):
    for j in range(6):
        if (l[i][j] == '.'):
            if (y[i][j] > maxm):
                maxm = y[i][j]
                maxi = i
                maxj = j
l[maxi][maxj] = 'P'
for i in range(6):
    print(l[i][0], l[i][1], '-', l[i][2], l[i][3], '-', l[i][4], l[i][5], sep='')
