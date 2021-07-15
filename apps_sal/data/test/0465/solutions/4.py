n, a, b = map(int, input().split())
if a > 1 < b or a * b == 1 and 1 < n < 4:
    print('NO')
else:
    z, o = ('01', '10')[a < b]
    l = [[z] * n for _ in range(n)]
    for i in range(n):
        l[i][i] = '0'
    for i in range(n - a * b):
        l[i][i + 1] = l[i + 1][i] = o
    print('YES')
    print('\n'.join(map(''.join, l)))
