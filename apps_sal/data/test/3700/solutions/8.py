3
(n, k) = list(map(int, input().split()))
if 2 * n + 1 < k:
    print(0)
else:
    print(min(n, k - 1) - (k + 2) // 2 + 1)
