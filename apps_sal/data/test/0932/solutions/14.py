n, m = map(int, input().split())
tab = [[int(i) for i in input().split()] for j in range(n)]
ans = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        z = 1
        for k in tab[i]:
            z = z and k
        for k in range(n):
            z = z and tab[k][j]
        ans[i][j] = z
tr = True
for i in range(n):
    for j in range(m):
        z = 0
        for k in ans[i]:
            z = z or k
        for k in range(n):
            z = z or ans[k][j]
        if z != tab[i][j] and tr:
            tr = False
            print('NO')
if tr:
    print('YES')
    for s in ans:
        for x in s:
            print(x, end=' ')
        print()
