n, k = map(int, input().split())
if n < k:
    ans = min(n, k - n)
elif n == k:
    ans = 0
else:
    ans = min(n % k, abs(n % k - k))
print(ans)
