n, k = map(int, input().split())
m = 6 * n - 1
print(m * k)
for i in range(n):
    for j in [1, 2, 3, 5]:
        print(k * (6 * i + j), end = ' ')
    print()

