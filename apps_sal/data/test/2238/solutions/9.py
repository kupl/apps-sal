n = int(input())
a = [['*'] * n for i in range(n)]
k = n // 2
cnt = n // 2 + 1
for i in range(n // 2 + 1):
    for j in range(k, cnt):
        a[i][j] = 'D'
    k -= 1
    cnt += 1
k += 2
cnt -= 2
for i in range(n // 2 + 1, n):
    for j in range(k, cnt):
        a[i][j] = 'D'
    k += 1
    cnt -= 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()
