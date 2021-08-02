n, k = list(map(int, input().split()))
if k > n // 2:
    k = n + 1 - k
print(2 * (k - 1) + 1 + k + 2 + 2 * (n - k - 1) + n)
