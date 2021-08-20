(n, c) = map(int, input().split())
xlist = []
for i in range(n):
    (x, v) = map(int, input().split())
    xlist.append((x, v))
fclock = [[0, 0] for _ in range(n)]
(ftemp, fval) = ([0] * n, [0] * n)
for i in range(n):
    if i == 0:
        fval[0] = xlist[i][1]
        if fval[i] - xlist[i][0] < 0:
            fclock[i] = [-1, 0]
        else:
            fclock[i] = [0, fval[0] - xlist[i][0]]
    else:
        fval[i] = fval[i - 1] + xlist[i][1]
        if fclock[i - 1][1] < fval[i] - xlist[i][0]:
            fclock[i] = [i, fval[i] - xlist[i][0]]
        else:
            fclock[i] = fclock[i - 1]
fret = [xlist[i][0] for i in range(n)]
rxlist = []
for i in range(n - 1, -1, -1):
    rxlist.append([c - xlist[i][0], xlist[i][1]])
rclock = [[0, 0] for _ in range(n)]
(rtemp, rval) = ([0] * n, [0] * n)
for i in range(n):
    if i == 0:
        rval[0] = rxlist[i][1]
        if rval[i] - rxlist[i][0] < 0:
            rclock[i] = [-1, 0]
        else:
            rclock[i] = [0, rval[0] - rxlist[i][0]]
    else:
        rval[i] = rval[i - 1] + rxlist[i][1]
        if rclock[i - 1][1] < rval[i] - rxlist[i][0]:
            rclock[i] = [i, rval[i] - rxlist[i][0]]
        else:
            rclock[i] = rclock[i - 1]
rret = [rxlist[i][0] for i in range(n)]
gmax = max(rclock[n - 1][1], fclock[n - 1][1])
for i in range(n - 1):
    tempg = fclock[i][1] + rclock[n - 2 - i][1]
    if fclock[i][0] < 0 or rclock[n - 2 - i][0] < 0:
        pass
    else:
        tempg -= min(fret[fclock[i][0]], rret[rclock[n - 2 - i][0]])
    gmax = max(gmax, tempg)
print(gmax)
