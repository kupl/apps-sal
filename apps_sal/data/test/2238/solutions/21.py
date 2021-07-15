n = int(input())
a = [['*' for i in range(n)] for i in range(n)]
k = 1
for i in range(0, n // 2 + 1):
    for j in range(n // 2, n // 2 + k):
        a[i][j] = 'D'
    a[i][0: n // 2] = reversed(a[i][n // 2 + 1: n])
    k += 1
k -= 2
for i in range(n // 2 + 1, n):
    for j in range(n // 2, n // 2 + k):
        a[i][j] = 'D'
    a[i][0: n // 2] = reversed(a[i][n // 2 + 1: n])
    k -= 1
for i in a:
    print(''.join(i))
