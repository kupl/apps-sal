(H, W, M) = map(int, input().split())
bombs = {}
rows = []
cols = []
for i in range(H):
    rows.append([i, 0])
for i in range(W):
    cols.append([i, 0])
for i in range(M):
    (y, x) = map(lambda x: x - 1, map(int, input().split()))
    bombs[y, x] = True
    rows[y][1] += 1
    cols[x][1] += 1
rows = sorted(rows, key=lambda x: x[1], reverse=True)
cols = sorted(cols, key=lambda x: x[1], reverse=True)
answer = 0
for row in rows:
    a = cols[0][1] + row[1] - (1 if (row[0], cols[0][0]) in bombs else 0)
    if a > answer:
        answer = a
for col in cols:
    a = rows[0][1] + col[1] - (1 if (rows[0][0], col[0]) in bombs else 0)
    if a > answer:
        answer = a
print(answer)
