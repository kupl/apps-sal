n, k, *_ = map(int, input().split(" "))
lc = [-1] * n
rc = [n] * n
tr = [-1] * n
br = [n] * n
b = [input() for _ in range(n)]
ans = [[0] * n for _ in range(n)]
pre, post = 0, 0

for i in range(n):
    for j in range(n):
        if b[i][j] == 'B':
            rc[i], br[j] = j, i
            if lc[i] == -1:
                lc[i] = j
            if tr[j] == -1:
                tr[j] = i
for i in range(n):
    if tr[i] == -1 and br[i] == n:
        pre += 1
    if lc[i] == -1 and rc[i] == n:
        pre += 1

for col in range(n - k + 1):
    tot = 0
    for row in range(k):
        if lc[row] >= col and rc[row] < col + k:
            tot += 1
    ans[0][col] = tot
    for row in range(1, n - k + 1):
        if lc[row - 1] >= col and rc[row - 1] < col + k:
            tot -= 1
        if lc[row + k - 1] >= col and rc[row + k - 1] < col + k:
            tot += 1
        ans[row][col] = tot
for row in range(n - k + 1):
    tot = 0
    for col in range(k):
        if tr[col] >= row and br[col] < row + k:
            tot += 1
    post = max(post, ans[row][0] + tot)
    for col in range(1, n - k + 1):
        if tr[col - 1] >= row and br[col - 1] < row + k:
            tot -= 1
        if tr[col + k - 1] >= row and br[col + k - 1] < row + k:
            tot += 1
        post = max(post, ans[row][col] + tot)

print(pre + post)
