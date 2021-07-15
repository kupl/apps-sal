n, m = [int(i) for i in input().split()]
sum1 = [0] * n
sum2 = [0] * m
res = [[0] * m for i in range(n)]
a = 0
k = [0] * 4
flag = False
for i in range(n):
    a = [int(i2) for i2 in input().split()]
    sum1[i] = sum(a)
    for i2 in range(m):
        sum2[i2] += a[i2]
for i in range(n):
    if sum1[i] == m:
        k[2] += 1
for i in range(m):
    if sum2[i] == n:
        k[3] += 1
for i in range(n):
    if (sum1[i] > k[3]) and not(sum1[i] == 0 or sum1[i] == m) or ((k[2] * k[3] == 0) and k[2] != k[3]):
        flag = True
for i in range(m):
    if (sum2[i] > k[2]) and not(sum2[i] == 0 or sum2[i] == n) or ((k[2] * k[3] == 0) and k[2] != k[3]):
        flag = True
if flag:
    print('NO')
else:
    print('YES')
    for i in range(n):
        for i2 in range(m):
            res[i][i2] = 1
    for i in range(m):
        if sum2[i] != n:
            for i2 in range(n):
                res[i2][i] = 0
    for i in range(n):
        if sum1[i] != m:
            for i2 in range(m):
                res[i][i2] = 0
    for i in range(n):
        for i2 in range(m):
            print(res[i][i2],end=' ')
        print()

