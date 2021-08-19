(n, k) = list(map(int, input().split()))
ans = 0
ans += k * (k - 1) ** (n - 1)
print(ans)
