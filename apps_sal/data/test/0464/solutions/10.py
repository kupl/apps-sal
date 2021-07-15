n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

flag = False

def check(x, y):
    if s[x-1][y-1] == s[x-1][y+1] == s[x+1][y-1] == s[x+1][y+1] == '.' and s[x-1][y] == s[x][y] == s[x+1][y] == s[x][y-1] == s[x][y+1] == '*':
        return True
    return False

def supercheck(x, y):
    k = 1
    i = x-1
    while i >= 0 and s[i][y] == '*':
        i -= 1
        k += 1

    i = x+1
    while i < n and s[i][y] == '*':
        i += 1
        k += 1

    i = y - 1
    while i >= 0 and s[x][i] == '*':
        i -= 1
        k += 1

    i = y + 1
    while i < m and s[x][i] == '*':
        i += 1
        k += 1

    true_k = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == '*':
                true_k += 1

    if true_k == k:
        return True
    return False


for i in range(1, n - 1):
    for j in range(1, m - 1):
        if s[i][j] != '*': continue
        if check(i, j):
            if supercheck(i, j):
                print('YES')
                return
            else:
                print('NO')
                return

print('NO')
