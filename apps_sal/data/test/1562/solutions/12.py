import sys
n, m, k, q = [int(i) for i in sys.stdin.readline().split()]
indata = sys.stdin.readlines()
data = []
inf = 1 << 50


for i in range(k):
    data.append(tuple([int(f) for f in indata[i].split()]))

data.sort()
chutes = [int(i) for i in indata[-1].split()]
chutes.sort()
nearch = [(0, 0)] * (m + 1)
for i in range(1, chutes[0] + 1):
    nearch[i] = (chutes[0], chutes[0])
for i in range(q - 1):
    a = chutes[i]
    b = chutes[i + 1]
    for j in range(a + 1, b):
        nearch[j] = (a, b)
    nearch[b] = (b, b)
for i in range(chutes[-1], m + 1):
    nearch[i] = (chutes[-1], chutes[-1])

lastr = -1
rows = []
rowdata = {}
for d in data:
    if d[0] != lastr:
        lastr = d[0]
        rows.append(d[0])
        rowdata[d[0]] = []
    rowdata[d[0]].append(d[1])


dp = [[(1, 0), (1, 0)]]
start = 0
if rows[0] == 1:
    dp[0] = [(rowdata[1][-1], rowdata[1][-1] - 1), (1, inf)]
    start = 1

lnr = len(rows)
for i in range(start, lnr):
    row = rowdata[rows[i]]
    LR = (0, inf)
    for f in range(4):
        ldp = dp[-1][f // 2]
        am = ldp[1]
        d = nearch[ldp[0]][f % 2]
        am += abs(ldp[0] - d)
        am += abs(d - row[0])
        am += row[-1] - row[0]

        if am < LR[1]:
            LR = (row[-1], am)

    RL = (0, inf)
    for f in range(4):
        ldp = dp[-1][f // 2]
        am = ldp[1]
        d = nearch[ldp[0]][f % 2]
        am += abs(ldp[0] - d)
        am += abs(d - row[-1])
        am += row[-1] - row[0]

        if am < RL[1]:
            RL = (row[0], am)
    dp.append([LR, RL])


print(min(dp[-1][0][1], dp[-1][1][1]) + rows[-1] - 1)
