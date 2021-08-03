n, k = list(map(int, input().split()))

if k <= n + 1:
    ans = (k - 1) // 2
else:
    ans = (k - 1) // 2 - (k - n - 1)

print(max(0, ans))
