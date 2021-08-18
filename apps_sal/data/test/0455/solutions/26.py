
n = int(input())
listXY = [list(map(int, input().split())) for _ in range(n)]
listUV = [[listXY[i][0] + listXY[i][1], listXY[i][0] - listXY[i][1]]for i in range(n)]

isOdd = listUV[0][0] % 2
canReach = 1
for i in range(1, n):
    if isOdd != listUV[i][0] % 2:
        canReach = 0
        break

if not canReach:
    print((-1))
else:
    offset = 2**31 - isOdd
    m = 32 - isOdd
    d = [2**i for i in range(32)]
    w = []
    for i in range(n):
        x, y = 0, 0
        u, v = listUV[i][0] + offset, listUV[i][1] + offset
        s = ''
        if not isOdd:
            s = 'L'
            x = x - 1
        for k in range(31):
            u //= 2
            v //= 2
            u1, v1 = u % 2, v % 2
            if u1 == 0 and v1 == 1:
                s += 'D'
                y = y - d[k]
            elif u1 == 0 and v1 == 0:
                s += 'L'
                x = x - d[k]
            elif u1 == 1 and v1 == 1:
                s += 'R'
                x = x + d[k]
            elif u1 == 1 and v1 == 0:
                s += 'U'
                y = y + d[k]
        w.append(s)
    print((32 - isOdd))
    s = ''
    if not isOdd:
        s = '1 '
    for i in range(31):
        s += str(d[i]) + ' '
    print(s)
    for i in range(n):
        print((w[i]))
