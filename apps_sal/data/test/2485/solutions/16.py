(h, w, m) = map(int, input().split())
row = [0] * (h + 1)
col = [0] * (w + 1)
bombs = set([])
for i in range(m):
    (a, b) = map(int, input().split())
    row[a] += 1
    col[b] += 1
    bombs.add((a, b))
(r, c) = (max(row), max(col))
(rcnt, ccnt) = (0, 0)
for v in row:
    if v == r:
        rcnt += 1
for v in col:
    if v == c:
        ccnt += 1
doubled = 0
for (i, j) in bombs:
    if row[i] == r and col[j] == c:
        doubled += 1
if doubled == rcnt * ccnt:
    print(r + c - 1)
else:
    print(r + c)
