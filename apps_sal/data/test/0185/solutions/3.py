(n, k) = map(int, input().split())
ans = 2 * n + 1
ans += n - 1 + min(k - 1, n - k)
print(ans)
