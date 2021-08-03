__author__ = 'Admin'


def f(n):
    return max(n[0], n[1])


t = True
x1, y1, x2, y2, x3, y3 = map(int, input().split())
m = [x1, y1, x2, y2, x3, y3]
m1 = [[x1, y1, 'A'], [x2, y2, 'B'], [x3, y3, 'C']]
m1.sort(key=f)
maxi = max(m1[-1][0], m1[-1][1])
mini = min(m1[-1][0], m1[-1][1])
maxj = max(m1[-2][1], m1[-2][0])
minj = min(m1[-2][1], m1[-2][0])
maxk = max(m1[0][1], m1[0][0])
mink = min(m1[0][1], m1[0][0])
s = m1[-1][2]
s1 = m1[-2][2]
s2 = m1[0][2]
matr = [[0] * maxi for i in range(maxi)]
for i in range(mini):
    for j in range(maxi):
        matr[i][j] = s
if maxj == maxi and mini + minj <= maxi:
    for i in range(mini, minj + mini):
        for j in range(maxj):
            matr[i][j] = s1
    if maxk == maxi and mini + minj + mink == maxi:
        for i in range(minj + mini, mink + minj + mini):
            for j in range(maxk):
                matr[i][j] = s2
    else:
        t = False
else:
    if maxj == maxi - mini:
        for i in range(mini, mini + maxj):
            for j in range(minj):
                matr[i][j] = s1
        if maxk == maxj and mink == maxi - minj:
            for i in range(mini, mini + maxk):
                for j in range(minj, minj + mink):
                    matr[i][j] = s2
        else:
            t = False
    elif minj == maxi - mini:
        for i in range(mini, mini + minj):
            for j in range(maxj):
                matr[i][j] = s1
        if mink == minj and maxk == maxi - maxj:
            for i in range(mini, mini + mink):
                for j in range(maxj, maxj + maxk):
                    matr[i][j] = s2
        elif maxk == minj and mink == maxi - maxj:
            for i in range(mini, mini + maxk):
                for j in range(maxj, maxj + mink):
                    matr[i][j] = s2
        else:
            t = False
    else:
        t = False
if t == True:
    print(maxi)
    for i in range(maxi):
        print(*matr[i], sep='')
else:
    print(-1)
