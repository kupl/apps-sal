(n, k) = map(int, input().split())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
m = n ** 2
for j in range(n):
    for i in range(n - k + 1):
        a[j][n - i - 1] = m - i
    m -= n - k + 1
c = n * k - n
while c > 0:
    a[(c - 1) % n][(c - 1) // n] = m
    c -= 1
    m -= 1
s = 0
for i in range(n):
    s += a[i][k - 1]
print(s)
for i in range(n):
    for j in range(n - 1):
        print(a[i][j], end=' ')
    print(a[i][n - 1])
