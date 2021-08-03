n, k = [int(i) for i in input().split()]
for i in range(100 * k + 100 * n):
    if i * (i + 1) == (n + k - i) * 2:
        print(n - i)
        break
