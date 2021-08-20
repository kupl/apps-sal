(n, k) = map(int, input().split())
print(sum((n // b * (b - k) + max(n % b - k + 1, 0) - (k < 1) for b in range(k + 1, n + 1))))
