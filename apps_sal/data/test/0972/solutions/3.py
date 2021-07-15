n,m = list(map(int, input().split()))

row, col_sum, row_sum, black = [], [], [], []
for i in range(n):
    row.append(input())
    t = [0]
    for j in range(m):
        t += [t[j] + (row[i][j] == 'B')]
    row_sum += [t]

d = [[0,1], [1,0], [-1,0], [0,-1]]
for i in range(n):
    for j in range(m):
        if row[i][j] is 'W':
            continue
        w = 0
        for di in d:
            x = i + di[0]
            y = j + di[1]
            if x < 0 or y < 0 or x >= n or y >= m: 
                w += 1 ; continue
            if row[x][y] is 'W': 
                w += 1
        if w > 0: black.append((i,j))    
for i in range(m):
    t = [0]
    for j in range(n):
        t += [t[j] + (row[j][i] == 'B')]
    col_sum += [t]

def row_check(r, s, e):
    if s > e: e, s = s, e
    return row_sum[r][e + 1] - row_sum[r][s] == e - s + 1

def col_check(c, s, e):
    if s > e: e,s = s,e
    return col_sum[c][e + 1] - col_sum[c][s] == e - s + 1

res = True
for i in black:
    for j in black:
        if i <= j:
            continue
        a = row_check(i[0], i[1], j[1]) and col_check(j[1], i[0], j[0])
        b = row_check(j[0], i[1], j[1]) and col_check(i[1], i[0], j[0])
        res = res and (a or b)
print('YES' if res else 'NO')

