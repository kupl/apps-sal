n, k = map(int, input().split())
for i in range(k - 1, 0, -1):
    if n % i == 0:
        print(k * n // i + i)
        return
