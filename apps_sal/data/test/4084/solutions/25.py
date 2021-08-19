(n, b, r) = list(map(int, input().split()))
m = n // (b + r)
last = min(n - (b + r) * m, b)
print(b * m + last)
