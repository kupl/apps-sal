mod = 998244353

n = int(input())
a = list(input())

ans = 0

l = 1
while l < n and a[l] == a[0]:
    l += 1

r = n - 1
while r >= 0 and a[r] == a[-1]:
    r -= 1

if l == n:
    cur = 1
    for i in range(n):
        cur *= (n - i)
        cur //= i + 1
        ans += cur
        ans %= mod
    print(ans)
    return

r = n - r - 1
if a[0] == a[-1]:
    ans += (l + 1) * (r + 1) % mod
else:
    ans += l + r + 1
    ans %= mod
print(ans)

