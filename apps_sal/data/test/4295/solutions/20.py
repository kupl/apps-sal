n, k = map(int, input().split())
if n >= k:
    ans = min(n % k, k - (n % k))
else:
    ans = min(n, k - n)
print(ans)
