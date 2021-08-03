3

n, k = tuple(map(int, input().split()))
if k <= n - n // 2:
    print(2 * k - 1)
else:
    print(2 * (k - n + n // 2))
