(n, k) = list(map(int, input().split()))
m = n // 2
x = m // (k + 1)
print(x, k * x, n - x - k * x)
