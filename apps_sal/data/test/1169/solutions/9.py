(n, m) = list(map(int, input().split()))
mini = max(0, n - 2 * m)
maxi = 10 ** 10
for i in range(n + 1):
    if i * (i - 1) // 2 < m:
        continue
    maxi = min(maxi, i)
print(mini, n - maxi)
