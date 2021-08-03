def read(): return list(map(int, input().split()))


n, m = read()
a = [list(read()) for i in range(n)]
b = [a[i][:] for i in range(n)]
flag = True
for i in range(n):
    c = sorted(b[i])
    d = b[i][:]
    dif = sum(c[j] != d[j] for j in range(m))
    if dif > 2:
        flag = False
if flag:
    print('YES')
    return
for k1 in range(m):
    for k2 in range(k1 + 1, m):
        b = [a[i][:] for i in range(n)]
        for i in range(n):
            b[i][k1], b[i][k2] = b[i][k2], b[i][k1]
        flag = True
        for i in range(n):
            c = sorted(b[i])
            d = b[i][:]
            dif = sum(c[j] != d[j] for j in range(m))
            if dif > 2:
                flag = False
        if flag:
            print('YES')
            return
print('NO')
