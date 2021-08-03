n, k = map(int, input().split())
ans = 0
if k == 0:
    print(n**2)
    return
for i in range(k + 1, n + 1):
    a = n - n % i
    ans += (i - k) * (a // i)
    if n % i >= k:
        ans += n % i - k + 1
print(ans)
