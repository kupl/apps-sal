n, k = (int(s) for s in input().split())
rows = []
for i in range(n):
    rows.append([c for c in input()])

def nbcnt(row, col):
    res = 0
    if col != 0 and rows[row][col - 1] == 'S':
        res += 1
    if col != 11 and rows[row][col + 1] == 'S':
        res += 1
    return res

for c in range(3):
    for i in range(n):
        for j in range(12):
            if k != 0 and rows[i][j] == '.' and nbcnt(i, j) == c:
                rows[i][j] = 'x'
                k -= 1

res = 0
for i in range(n):
    for j in range(12):
        if rows[i][j] != '.' and rows[i][j] != '-':
            res += nbcnt(i, j)

print(res)

for i in range(n):
    print("".join(rows[i]))

