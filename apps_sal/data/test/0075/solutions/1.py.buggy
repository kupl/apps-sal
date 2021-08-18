n, m = list(map(int, input().split()))
a = [input() for i in range(n)]
cntx = [0] * n
cnty = [0] * m
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            cntx[i] += 1
            cnty[j] += 1
            cnt += 1
for i in range(n):
    for j in range(m):
        cur = cntx[i] + cnty[j] - int(a[i][j] == '*')
        if cur == cnt:
            print('YES')
            print(i + 1, j + 1)
            return
print('NO')
