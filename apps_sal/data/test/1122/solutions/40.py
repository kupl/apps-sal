(n, m) = map(int, input().split())
(x, y) = ((m + 1) // 2, m // 2)
for i in range(x):
    print(1 + i, 2 * x - i)
for i in range(y):
    print(2 * x + 1 + i, 2 * x + 1 + 2 * y - i)
