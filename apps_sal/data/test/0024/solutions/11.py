field = []
for _ in range(10):
    field.append(input())
rows = [row for row in field]
columns = []
for i in range(10):
    s = ''
    for j in range(10):
        s += field[j][i]
    columns.append(s)
maindiags = []
for k in range(-9, 10):
    s = ''
    if k >= 0:
        for i in range(10 - k):
            for j in range(k, 10):
                if i == j - k:
                    s += field[i][j]
    else:
        for i in range(-k, 10):
            for j in range(10 + k):
                if i == j - k:
                    s += field[i][j]
    maindiags.append(s)
diags = []
for k in range(-9, 10):
    s = ''
    if k >= 0:
        for i in range(k, 10):
            for j in range(k, 10):
                if i == 9 - j + k:
                    s += field[i][j]
    else:
        for i in range(10 + k):
            for j in range(10 + k):
                if i == 9 - j + k:
                    s += field[i][j]
    diags.append(s)


def answer(a):
    patterns = ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.']
    for elem in a:
        if len(elem) >= 5:
            for k in range(5):
                for i in range(len(elem) - 4):
                    flag = True
                    for j in range(5):
                        if elem[i + j] != patterns[k][j]:
                            flag = False
                    if flag:
                        return True
    return False


a = rows + columns + maindiags + diags
print('YES' if answer(a) else 'NO')
