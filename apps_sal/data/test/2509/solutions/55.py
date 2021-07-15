n, k = list(map(int, input().split()))
if k == 0:
    print((n**2))
    return
ans = 0
for i in range(k, n+1):
    p = n // i
    r = n % i
    ans += p * (i - k) + max(0, (r - k + 1))

print(ans)

