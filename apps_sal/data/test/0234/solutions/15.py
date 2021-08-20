(n, m) = [int(s) for s in input().split(' ')]
a = []
a.append('x' * (m + 2))
for i in range(n):
    a.append(('x' + input() + 'x').replace('.', '0'))
a.append('x' * (m + 2))
n = n + 2
m = m + 2
all_ok = True
for i in range(1, n - 1):
    if not all_ok:
        break
    for j in range(1, m - 1):
        if not all_ok:
            break
        if a[i][j] == 'x' or a[i][j] == '*':
            continue
        ssum = 0
        for p in range(-1, 2):
            for q in range(-1, 2):
                if p == 0 and q == 0:
                    continue
                if a[i + p][j + q] == '*':
                    ssum = ssum + 1
        if str(ssum) != a[i][j]:
            all_ok = False
            break
if all_ok:
    print('YES')
else:
    print('NO')
