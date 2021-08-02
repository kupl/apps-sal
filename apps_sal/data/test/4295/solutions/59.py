n, k = map(int, input().split())
i = n // k
a = abs(n - k * i)
b = abs(n - k * (i + 1))
print(min(a, b))
