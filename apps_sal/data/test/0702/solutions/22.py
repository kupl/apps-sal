n = int(input())
tab = []
for i in range(n):
    a = list(input())
    tab.append(a)
for i in range(i):
    for j in range(n):
        if 0 < i < n - 1 and 0 < j < n - 1 and tab[i - 1][j] == tab[i + 1][j] == tab[i][j + 1] == tab[i][j - 1] == tab[i][j] == '.':
            tab[i][j] = '#'
            tab[i - 1][j] = '#'
            tab[i + 1][j] = '#'
            tab[i][j - 1] = '#'
            tab[i][j + 1] = '#'
for i in range(n):
    for j in range(n):
        if tab[i][j] == '.':
            print('NO')
            return
print('YES')
