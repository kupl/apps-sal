n, k, x, y = [int(input()) for _ in range(4)]
if n <= k:
    print(x * n)
else:
    print(x * k + y * (n - k))
