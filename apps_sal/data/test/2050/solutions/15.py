(n, k) = map(int, input().split())
print(k * (6 * (n - 1) + 5))
for i in range(0, n):
    print(k * (6 * i + 1), k * (6 * i + 2), k * (6 * i + 3), k * (6 * i + 5))
