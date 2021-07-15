m, n = map(int, input().split())
row = [True] * m
col = [True] * n
a = [[0] * n for _ in range(m)]
for i in range(m):
    s = list(map(int, input().split()))
    for j in range(n):
        if (s[j] == 0):
            row[i] = False
            col[j] = False
        a[i][j] = s[j]
c = 0
r = 0
for i in range(n):
    if col[i]:
        c+=1
for j in range(m):
    if row[j]:
        r+=1
res = []
if (r > 0 and c > 0) or (r == 0 and c == 0):
    for i in range(m):
        res.append([])
        for j in range(n):
            if col[j] and row[i]:
                res[i].append(1)
            elif a[i][j] == 0 or (col[j] or row[i]):
                res[i].append(0)
            else:
                print('NO')
                return

    print('YES')
    for i in range(m):
        s = ' '.join(list(map(str, res[i])))
        print(s)
else:
    print('NO')
