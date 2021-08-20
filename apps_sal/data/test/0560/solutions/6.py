(n, m) = [int(x) for x in input().split()]
a = []
ans = 0
for i in range(n):
    a.append(list(input()))
for i in range(n):
    flag = 1
    for j in range(m):
        if a[i][j] == 'S':
            flag = 0
    if flag == 1:
        for j in range(m):
            a[i][j] = 'T'
for i in range(m):
    flag = 1
    for j in range(n):
        if a[j][i] == 'S':
            flag = 0
    if flag == 1:
        for j in range(n):
            a[j][i] = 'T'
for i in range(n):
    for j in range(m):
        if a[i][j] == 'T':
            ans += 1
print(ans)
