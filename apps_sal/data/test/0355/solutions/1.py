z = []
for i in range(8):
    z.append(input())
(a, b) = (9, 9)
for i in range(8):
    for j in range(8):
        if z[i][j] == 'W':
            sedi = True
            for r in range(0, i):
                if z[r][j] == 'B':
                    sedi = False
                    break
            if sedi:
                a = min(a, i)
        elif z[i][j] == 'B':
            sedi = True
            for r in range(i + 1, 8):
                if z[r][j] == 'W':
                    sedi = False
                    break
            if sedi:
                b = min(b, 7 - i)
print('A' if a <= b else 'B')
