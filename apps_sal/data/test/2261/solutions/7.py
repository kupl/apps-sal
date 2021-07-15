Not = lambda x: '+' if x == '*' else '*'
k = int(input())
n = 2 ** k
a = [['+'] * n for i in range(n)]
for p in range(k):
    n = 2 ** p
    for i in range(n):
        for j in range(n):
            a[i][j + n] = a[i][j]
            a[i + n][j] = a[i][j]
            a[i + n][j + n] = Not(a[i][j])
[print(''.join(map(str, i))) for i in a]

