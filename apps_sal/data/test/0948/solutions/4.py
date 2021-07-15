n, m = map(int, input().split())
a = [input().replace('', ' ').split() for i in range(n)]
res = 0
for i in range(n - 1):
    for j in range(m - 1):
        s = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
        if sorted(s) ==  ['a', 'c', 'e', 'f']: res += 1
print(res)
