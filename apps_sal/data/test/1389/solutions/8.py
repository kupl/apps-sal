(n, m) = list(map(int, input().split(' ')))
p = [input() for i in range(n)]
p1 = [[1 if p[i][j] == 'B' else -1 for j in range(m)] for i in range(n)]
tm = [0 for i in range(m)]
r = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if tm[j] != p1[i][j]:
            r = r + 1
            tp = p1[i][j] - tm[j]
            for l in range(j + 1):
                tm[l] = tm[l] + tp
print(r)
