(h, w) = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
p = [[0] * (w + 2) for i in range(h + 2)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            p[i][j] += 1
            p[i][j + 1] += 1
            p[i][j + 2] += 1
            p[i + 1][j] += 1
            p[i + 1][j + 2] += 1
            p[i + 2][j] += 1
            p[i + 2][j + 1] += 1
            p[i + 2][j + 2] += 1
for m in range(1, h + 1):
    for n in range(1, w + 1):
        i = m - 1
        j = n - 1
        if s[i][j] == '#':
            p[m][n] = '#'
for m in range(1, h + 1):
    print(''.join(map(str, p[m][1:w + 1])))
