n, k = map(int, input().split())
k = abs(k)
print(sum(min(i - 1, 2 * n - i + 1) * min(j - 1, 2 * n - j + 1) for i, j in zip(range(2 + k, n * 2 + 1), range(2, n * 2 + 1 - k))))
