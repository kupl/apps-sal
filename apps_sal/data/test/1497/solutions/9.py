n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    t = a[i]
    a[i] = []
    for j in range(n):
        a[i].append(t[j] == '1')
maxRes = -1
for i in range(n):
    s = []
    b = a[:]
    for j in range(n):
        s.append(not a[i][j])
        b[i][j] = True
    for j in range(i):
        for k in range(n):
            if s[k]:
                b[j][k] = not b[j][k]
    for j in range(i + 1, n):
        for k in range(n):
            if s[k]:
                b[j][k] = not b[j][k]
    res = 0
    for j in range(n):
        t = True
        for k in range(n):
            if not b[j][k]:
                t = False
        if t:
            res += 1
    maxRes = max(maxRes, res)
print(maxRes)
