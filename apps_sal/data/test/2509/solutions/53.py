n, k = map(int, input().split())
print(sum(n // b * (b - k) + max(n % b - k + (k > 0), 0) for b in range(k + 1, n + 1)))
