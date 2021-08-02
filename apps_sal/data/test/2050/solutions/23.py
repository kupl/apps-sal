n, k = map(int, input().split())
print(k * (6 * n - 1))
for i in range(1, n + 1):
    x = (i - 1) * 6 + 1
    print(k * x, end=' ')
    print(k * (x + 1), end=' ')
    print(k * (x + 2), end=' ')
    print(k * (x + 4))
