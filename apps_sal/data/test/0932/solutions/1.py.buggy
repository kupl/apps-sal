n, m = list(map(int, input().split()))
a = [[0 for x in range(0, 200)] for x in range(0, 200)]

for i in range(0, n):
    b = input()
    a[i] = b.split(' ')

for i in range(0, n):
    for j in range(0, m):
        a[i][j] = int(a[i][j])

ans = [[1 for x in range(0, 200)] for x in range(0, 200)]

for i in range(0, n):
    for j in range(0, m):
        if(a[i][j] == 0):
            for i1 in range(0, n):
                ans[i1][j] = 0
            for j1 in range(0, m):
                ans[i][j1] = 0

b = [[1 for x in range(0, 200)] for x in range(0, 200)]

for i in range(0, n):
    for j in range(0, m):
        b[i][j] = 0
        for j1 in range(0, m):
            b[i][j] = b[i][j] | ans[i][j1]
        for i1 in range(0, n):
            b[i][j] = b[i][j] | ans[i1][j]
        if(b[i][j] != a[i][j]):
            print('NO')
            return

print('YES')
for i in range(0, n):
    res = ''
    for j in range(0, m):
        res = res + str(ans[i][j])
        res = res + ' '
    print(res)
