(n, k) = list(map(int, input().split()))
k = abs(k)
result = 0
for p in range(k + 2, 2 * n + 1):
    if p <= n + 1:
        result = result + (p - 1) * (p - k - 1)
    elif n + 2 <= p <= n + k + 1:
        result = result + (2 * n - p + 1) * (p - k - 1)
    else:
        result = result + (2 * n - p + 1) * (2 * n - p + k + 1)
print(result)
