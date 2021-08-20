(n, k, x, y) = [int(input()) for _ in range(4)]
print([n * x, k * x + (n - k) * y][n - k > 0])
