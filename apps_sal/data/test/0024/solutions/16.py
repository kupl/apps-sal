r = [input() for _ in range(10)]
c = []
for i in range(10):
    t = ''
    for j in range(10):
        t += r[j][i]
    c.append(t)
for x in r:
    if any((s in x for s in ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.'])):
        print('YES')
        quit()
else:
    for y in c:
        if any((s in y for s in ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.'])):
            print('YES')
            quit()
    else:
        for a in range(6):
            z1 = ''
            z2 = ''
            for b in range(10 - a):
                z1 += r[a + b][b]
                z2 += r[b][a + b]
            if any((s in z1 for s in ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.'])):
                print('YES')
                quit()
            if any((s in z2 for s in ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.'])):
                print('YES')
                quit()
        c = list(zip(*r[::-1]))
        for a in range(6):
            z1 = ''
            z2 = ''
            for b in range(10 - a):
                z1 += c[a + b][b]
                z2 += c[b][a + b]
            if any((s in z1 for s in ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.'])):
                print('YES')
                quit()
            if any((s in z2 for s in ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.'])):
                print('YES')
                quit()
    print('NO')
