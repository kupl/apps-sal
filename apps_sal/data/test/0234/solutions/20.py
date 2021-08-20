(n, m) = [int(x) for x in input().split()[:2]]
fd = [[-2 for i in range(m)] for i in range(n)]


def inbd(i, j):
    if i >= 0 and i < n and (j >= 0) and (j < m):
        return (i, j)
    else:
        return None


def neis(i, j):
    ans = [inbd(i - 1, j - 1), inbd(i - 1, j), inbd(i - 1, j + 1), inbd(i, j - 1), inbd(i, j + 1), inbd(i + 1, j - 1), inbd(i + 1, j), inbd(i + 1, j + 1)]
    ans = [x for x in ans if x != None]
    return ans


for i in range(n):
    s = input()
    for j in range(m):
        c = s[j]
        if c == '*':
            fd[i][j] = '*'
        elif c == '.':
            fd[i][j] = 0
        else:
            fd[i][j] = int(c)
for i in range(n):
    for j in range(m):
        if fd[i][j] == '*':
            for (x, y) in neis(i, j):
                if fd[x][y] == '*':
                    continue
                fd[x][y] -= 1
fg = True
for i in range(n):
    for j in range(m):
        if fd[i][j] == '*' or fd[i][j] == 0:
            continue
        else:
            fg = False
if fg:
    print('YES')
else:
    print('NO')
