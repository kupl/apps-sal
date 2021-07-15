n, a, b = list(map(int, input().split()))
z, o = ('01', '10')[a < b]
n *= not (a > 1 < b or 1 < n * a * b < 4)
l = [[z] * n for _ in range(n)]
for i in range(n):
    l[i][i] = '0'
for i in range(n - a * b):
    l[i][i + 1] = l[i + 1][i] = o
print(('YES', 'NO')[not n])
print('\n'.join(map(''.join, l)))


