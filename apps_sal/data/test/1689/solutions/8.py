N = int(input())
rows = []
for i in range(N):
    rows.append(input().split('|'))
flg = False
for (i, row) in enumerate(rows):
    if row[0] == 'OO':
        rows[i][0] = '++'
        flg = True
    elif row[1] == 'OO':
        rows[i][1] = '++'
        flg = True
    if flg:
        break
if not flg:
    print('NO')
else:
    print('YES')
    for row in rows:
        print('{}|{}'.format(row[0], row[1]))
