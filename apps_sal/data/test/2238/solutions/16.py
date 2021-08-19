n = int(input())
a = [['D'] * n for x in range(n)]
for i in range(n):
    star = abs(n - ((i + 1) * 2 - 1))
    for j in range(star // 2):
        a[i][j] = '*'
        a[i][-j - 1] = '*'
for x in a:
    print(*x, sep='')
