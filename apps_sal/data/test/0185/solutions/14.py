n, k = list(map(int, input().split()))
ans = 0
if k != 1 and k != n:
    ans = 2 * min(k - 1, n - k) + max(k - 1, n - k) + 2 * n + 1
else:
    ans = 3 * n
print(ans)
