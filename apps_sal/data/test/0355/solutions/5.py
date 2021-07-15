p = []
for i in range(8):
    p.append(list(input()))
minb = 999999999
minch = 999999999
for i in range(8):
    for t in range(8):
        if p[i][t] == 'W':
            s = 0
            for e in range(i - 1, -1, -1):
                if p[e][t] != '.':
                    s = 999999
                else:
                    s += 1
            minb = min(minb, s)
        elif p[i][t] == 'B':
            s = 0
            for e in range(i + 1, 8):
                if p[e][t] != '.':
                    s = 999999
                else:
                    s += 1
            minch = min(minch, s)
if minb <= minch:
    print('A')
else:
    print('B')

