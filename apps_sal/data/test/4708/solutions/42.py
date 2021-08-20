(n, k, x, y) = [int(input()) for _ in range(4)]
ans = k * x + (n - k) * y
print(ans if n > k else n * x)
