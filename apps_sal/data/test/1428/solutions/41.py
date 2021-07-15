n, C = map(int, input().split())
d = []
for i in range(C):
    d.append(list(map(int, input().split())))
c = []
for i in range(n):
    c.append(list(map(int, input().split())))
c0 = {}
c1 = {}
c2 = {}
for i in range(0, n * 2 - 1, 3):
    for j in range(max(0, i - n + 1), min(n, i + 1)):
        c0.setdefault(c[j][i - j], 0)
        c0[c[j][i - j]] += 1
for i in range(1, n * 2 - 1, 3):
    for j in range(max(0, i - n + 1), min(n, i + 1)):
        c1.setdefault(c[j][i - j], 0)
        c1[c[j][i - j]] += 1
for i in range(2, n * 2 - 1, 3):
    for j in range(max(0, i - n + 1), min(n, i + 1)):
        c2.setdefault(c[j][i - j], 0)
        c2[c[j][i - j]] += 1
D = []
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or k == i:
                continue
            temp = 0
            for p, q in c0.items():
                temp += d[p - 1][i] * q
            for p, q in c1.items():
                temp += d[p - 1][j] * q
            for p, q in c2.items():
                temp += d[p - 1][k] * q
            D.append(temp)
print(min(D))
