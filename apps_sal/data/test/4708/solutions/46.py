(n, k, x, y) = (int(input()), int(input()), int(input()), int(input()))
if n < k:
    print(x * n)
else:
    print(x * k + y * (n - k))
