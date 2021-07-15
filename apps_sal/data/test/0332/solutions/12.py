n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

ok = 'YES'
for i in range(m - 1 + n - 1 + 1):
    d = dict()
    for x in range(min(i + 1, m)):
        if i - x < n:
            if a[i - x][x] in d:
                d[a[i - x][x]] += 1
            else:
                d[a[i - x][x]] = 1
    for x in range(min(i + 1, m)):
        if i - x < n:
            if b[i - x][x] in d:
                d[b[i - x][x]] -= 1
                if d[b[i - x][x]] == 0:
                    d.__delitem__(b[i - x][x])
            else:
                print('NO')
                return
print('YES')

