n = int(input())
rows = []
evils = 0
for i in range(n):
    rows.append(input())
columns = []
for i in range(n):
    L = []
    for j in range(n):
        L.append(rows[j][i])
    columns.append(L)
can = True
for i in range(n):
    if not can:
        break
    for j in range(n):
        if rows[i][j] == '.':
            continue
        r = '.' not in rows[i]
        c = '.' not in columns[j]
        if r and c:
            can = False
            break
if not can:
    print(-1)
else:
    used = 'rows'
    for i in range(n):
        if rows[i].count('E') == n:
            used = 'columns'
            break
        elif columns[i].count('E') == n:
            used = 'rows'
            break
    if used == 'rows':
        for i in range(n):
            x = rows[i].index('.')
            print(i + 1, end=' ' + str(x + 1) + '\n')
    else:
        for i in range(n):
            x = columns[i].index('.')
            print(x + 1, end=' ' + str(i + 1) + '\n')
