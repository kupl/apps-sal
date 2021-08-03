field = [input() for i in range(4)]
for i in range(3):
    for j in range(3):
        s = ''
        for a in range(2):
            for b in range(2):
                s += field[i + a][j + b]
        if s.count('.') != 2:
            print('YES')
            return
print('NO')
