n, m, k = list(map(int, input().split()))
b = [list(map(int, input().split())) for i in range(n)]
t = [[None for i in range(m)] for j in range(n)]
t2 = [[None for i in range(m)] for j in range(n)]

t[0][0] = {b[0][0]: 1}
for i in range(1, m):
    t[0][i] = {list(t[0][i - 1].keys())[0] ^ b[0][i]: 1}
for i in range(1, n):
    t[i][0] = {list(t[i - 1][0].keys())[0] ^ b[i][0]: 1}


limit = (n + m - 2) // 2

for i in range(1, n):
    for j in range(1, m):
        if i + j > limit:
            continue
        t[i][j] = {}
        for num, cnt in list(t[i - 1][j].items()):
            t[i][j][num ^ b[i][j]] = cnt
        for num, cnt in list(t[i][j - 1].items()):
            if num ^ b[i][j] in list(t[i][j].keys()):
                t[i][j][num ^ b[i][j]] += cnt
            else:
                t[i][j][num ^ b[i][j]] = cnt

for i in range(n):
    for j in range(m):
        if i + j == limit:
            b[i][j] = 0

t2[n - 1][m - 1] = {b[n - 1][m - 1]: 1}
for i in range(m - 2, -1, -1):
    t2[n - 1][i] = {list(t2[n - 1][i + 1].keys())[0] ^ b[n - 1][i]: 1}
for i in range(n - 2, -1, -1):
    t2[i][m - 1] = {list(t2[i + 1][m - 1].keys())[0] ^ b[i][m - 1]: 1}


for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        if i + j < limit:
            continue
        t2[i][j] = {}
        for num, cnt in list(t2[i + 1][j].items()):
            t2[i][j][num ^ b[i][j]] = cnt
        for num, cnt in list(t2[i][j + 1].items()):
            if num ^ b[i][j] in list(t2[i][j].keys()):
                t2[i][j][num ^ b[i][j]] += cnt
            else:
                t2[i][j][num ^ b[i][j]] = cnt

res = 0


for i in range(n):
    for j in range(m):
        if i + j != limit:
            continue
        tk = set(t[i][j].keys())
        for k2 in list(t2[i][j].keys()):
            if (k2 ^ k) in tk:
                res += t2[i][j][k2] * t[i][j][k2 ^ k]

print(res)
