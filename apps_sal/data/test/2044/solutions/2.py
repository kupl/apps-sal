(n, m) = map(int, input().split())
a = list(map(int, input().split()))
x = a[0]
y = 0
for i in range(n - 1):
    print(x // m - y // m, end=' ')
    x += a[i + 1]
    y += a[i]
print(x // m - y // m, end=' ')
