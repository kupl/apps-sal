n, m, k = list(map(int, input().split()))

rows = [[0, 0] for i in range(n)]
cols = [[0, 0] for i in range(m)]
for i in range(k):
    typ, p, x = list(map(int, input().split()))
    if typ == 1:
        rows[p-1] = [x, i+1]
    elif typ == 2:
        cols[p-1] = [x, i+1]
    else:
        print('WTF?!')

for i in range(n):
    line = []
    for j in range(m):
        if rows[i][1] > cols[j][1]:
            line.append(rows[i][0])
        else:
            line.append(cols[j][0])
    print(' '.join(map(str, line)))

