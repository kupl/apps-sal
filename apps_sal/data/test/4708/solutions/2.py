(n, k, x, y) = [int(input()) for _ in range(4)]
if k <= n:
    sum = x * k + y * (n - k)
else:
    sum = x * n
print(sum)
