n, k = map(int, input().split())
print((6 * n - 1) * k)
for i in range(1, 6 * n, 6):
    print(i * k, (i + 2) * k, (i + 3) * k, (i + 4) * k)
