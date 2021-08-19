(n, m) = map(int, input().split())
a = [input().split() for _ in range(n)]
mk = [[0] * m for _ in range(n)]
ans = []
for i in range(n - 1):
    for j in range(m - 1):
        if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1] == '1':
            ans.append((i + 1, j + 1))
            mk[i][j] = mk[i + 1][j] = mk[i][j + 1] = mk[i + 1][j + 1] = 1
if any((a[i][j] == '1' and (not mk[i][j]) for i in range(n) for j in range(m))):
    print(-1)
else:
    print(len(ans))
    print(*('%d %d' % (i, j) for (i, j) in ans), sep='\n')
