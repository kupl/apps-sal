(n, k) = list(map(int, input().split()))
ans = n + 1 + n + min(n - k, k - 1) + (n - 1)
print(ans)
