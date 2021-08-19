def R():
    return list(map(int, input().split()))


(n, m) = R()
rs = 0
a = []
for i in range(n):
    a.append(input())
for i in range(n - 1):
    for j in range(m - 1):
        c = []
        c.append(a[i][j])
        c.append(a[i + 1][j])
        c.append(a[i][j + 1])
        c.append(a[i + 1][j + 1])
        u = set(c)
        if len(u) == 4:
            if 'f' in u:
                if 'a' in u:
                    if 'c' in u:
                        if 'e' in u:
                            rs += 1
print(rs)
