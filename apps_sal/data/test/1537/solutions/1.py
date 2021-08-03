n, k = map(int, input().split())
board = [input() for _ in range(n)]
columns = [[0] * n for _ in range(n)]
rows = [[0] * n for _ in range(n)]
whites = 0
for i in range(n):
    first = -1
    last = 0
    flag = False
    for pos in range(n):
        if flag == False:
            if board[i][pos] == 'B':
                first = pos
                flag = True
        else:
            if board[i][pos] == 'B':
                last = pos
    if first == -1:
        whites += 1
        continue
    if last == 0:
        last = first
    if last - first < k:
        for j in range(max(0, last - k + 1), first + 1):
            columns[i][j] += 1
for i in range(n):
    first = -1
    last = 0
    flag = False
    for pos in range(n):
        if flag == False:
            if board[pos][i] == 'B':
                first = pos
                flag = True
        else:
            if board[pos][i] == 'B':
                last = pos
    if first == -1:
        whites += 1
        continue
    if last == 0:
        last = first
    if last - first < k:
        for j in range(max(0, last - k + 1), first + 1):
            rows[j][i] += 1
ccounts = [[0] * n for _ in range(n)]
rcounts = [[0] * n for _ in range(n)]
for i in range(n):
    tmp = 0
    for j in range(k):
        tmp += columns[j][i]
    ccounts[0][i] = tmp
    for j in range(1, n - k + 1):
        tmp += columns[j + k - 1][i]
        tmp -= columns[j - 1][i]
        ccounts[j][i] = tmp
for i in range(n):
    tmp = 0
    for j in range(k):
        tmp += rows[i][j]
    rcounts[i][0] = tmp
    for j in range(1, n - k + 1):
        tmp += rows[i][j + k - 1]
        tmp -= rows[i][j - 1]
        rcounts[i][j] = tmp
ans = whites
for x in range(n):
    for y in range(n):
        tmp = whites
        tmp += ccounts[x][y]
        tmp += rcounts[x][y]
        ans = max(ans, tmp)
print(ans)
