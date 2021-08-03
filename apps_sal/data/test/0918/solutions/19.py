n, m = list(map(int, input().split(' ')))
b = {}
pb = {}
ppb = {}
for i in range(n):
    curline = input().split(' ')
    name = curline[0]
    com, ball = list(map(int, curline[1:3]))
    x = name, ball
    if com in b:
        if x[1] > b[com][1]:
            b[com], x = x, b[com]
        if com in pb:
            if x[1] > pb[com][1]:
                pb[com], x = x, pb[com]
            if com in ppb:
                if x[1] > ppb[com][1]:
                    ppb[com], x = x, ppb[com]
            else:
                ppb[com] = x
        else:
            pb[com] = x
    else:
        b[com] = x

for com in range(1, m + 1):
    if com in ppb and ppb[com][1] == pb[com][1]:
        print('?')
    else:
        print(b[com][0], pb[com][0])
