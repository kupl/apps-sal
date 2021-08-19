(n, m) = list(map(int, input().split(' ')))
f = []
for i in range(0, n, 2):
    f.append(['#'] * m)
    if i + 1 < n:
        f.append(['.'] * m)
p = m - 1
for i in range(1, n, 2):
    f[i][p] = '#'
    p = 0 if p == m - 1 else m - 1
for r in f:
    print(''.join(r))
