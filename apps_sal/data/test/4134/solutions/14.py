n, m, k = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
if n > m:
    d = []
    for i in range(m):
        d.append([])
        for j in range(n):
            d[i].append(a[j][i])
    a = d
    n, m = m, n

b = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append([])
    b.append(temp)
for i in range((n + m) // 2):
    for j in range(min(i + 1, m, n)):
        if i == 0:
            b[j][i - j].append(a[j][i - j])
        elif j == 0:
            b[j][i - j].append(b[j][i - j - 1][0] ^ a[j][i - j])
        elif j == i:
            b[j][i - j].append(b[j - 1][i - j][0] ^ a[j][i - j])
        else:
            for x in b[j][i - j - 1] + b[j - 1][i - j]:
                b[j][i - j].append(x ^ a[j][i - j])
c = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append([])
    c.append(temp)
for i in range((n + m + 1) // 2):
    for j in range(min(i + 1, m, n)):
        if i == 0:
            c[(n - 1) - j][(m - 1) - (i - j)].append(k)
        elif j == 0:
            c[(n - 1) - j][(m - 1) - (i - j)].append(c[(n - 1) - j][(m - 1) - (i - j - 1)][0] ^ a[(n - 1) - j][(m - 1) - (i - j - 1)])
        elif j == i:
            c[(n - 1) - j][(m - 1) - (i - j)].append(c[(n - 1) - (j - 1)][(m - 1) - (i - j)][0] ^ a[(n - 1) - (j - 1)][(m - 1) - (i - j)])
        else:
            for x in c[(n - 1) - j][(m - 1) - (i - j - 1)]:
                c[(n - 1) - j][(m - 1) - (i - j)].append(x ^ a[(n - 1) - j][(m - 1) - (i - j - 1)])
            for x in c[(n - 1) - (j - 1)][(m - 1) - (i - j)]:
                c[(n - 1) - j][(m - 1) - (i - j)].append(x ^ a[(n - 1) - (j - 1)][(m - 1) - (i - j)])

wae = 0
i = (n + m) // 2 - 1
for j in range(min(m, n)):
    d = {}
    e = {}
    for l1 in b[j][i - j]:
        if not l1 in d:
            d[l1] = 0
        d[l1] += 1
    for l2 in c[j][i - j]:
        if not l2 in e:
            e[l2] = 0
        e[l2] += 1
    for key in list(d.keys()):
        if key in d and key in e:
            wae += d[key] * e[key]

print(wae)

