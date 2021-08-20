(n, k) = map(int, input().split())
ans = n * 3
u = min(n - k, k - 1)
ans = ans + u
print(ans)
