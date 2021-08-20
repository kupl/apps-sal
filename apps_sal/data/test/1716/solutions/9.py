(n, m, q) = list(map(int, input().split()))
table = [[0] * n for i in range(n)]
for i in range(m):
    (l, r) = list(map(int, input().split()))
    l -= 1
    r -= 1
    table[r][l] += 1
for i in range(n):
    for j in range(1, n):
        table[i][j] = table[i][j] + table[i][j - 1]
for i in range(n):
    for j in range(1, n):
        table[j][i] = table[j][i] + table[j - 1][i]
for i in range(q):
    (l, r) = list(map(int, input().split()))
    l -= 1
    r -= 1
    if l != 0:
        ans = table[r][r] - table[r][l - 1]
    else:
        ans = table[r][r]
    print(ans)
