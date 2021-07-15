def min_row():
    ans = 0
    for i in range(n):
        ans += min(a[i])
    return ans


def min_col():
    ans = 0
    for i in range(m):
        mm = 10000
        for j in range(n):
            mm = min(mm, a[j][i])
        ans += mm
    return ans


def remove_cols():
    ans = 0
    min_col = [0] * m
    for i in range(m):
        min_col[i] = 1000
        for j in range(n):
            min_col[i] = min(min_col[i], a[j][i])
        ans += min_col[i]
        for j in range(n):
            a[j][i] -= min_col[i]
    return ans, min_col


def remove_rows():
    ans = 0
    min_row = []
    for i in range(n):
        min_row.append(min(a[i]))
        ans += min_row[-1]
        for j in range(m):
            a[i][j] -= min_row[i]
    return ans, min_row


n, m = list(map(int, input().split()))
a = []
s = 0

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    s += sum(row)

rows = min_row()
cols = min_col()

if rows == 0 and cols == 0:
    if s == 0:
        print(0)
        return
    else:
        print(-1)
        return

if cols == 0 or (rows != 0 and (s - rows * m) % n == 0 and ((s - cols * n) % m != 0 or (s - rows * m) // n + rows < (s - cols * n) // m + cols)):
    ans, min_row = remove_rows()
    ans1, min_col = remove_cols()
else:
    ans1, min_col = remove_cols()
    ans, min_row = remove_rows()

ans += ans1

for row in a:
    for ai in row:
        if ai != 0:
            print(-1)
            return

print(ans)
for i in range(n):
    for j in range(min_row[i]):
        print("row", i + 1)
for i in range(m):
    for j in range(min_col[i]):
        print("col", i + 1)

