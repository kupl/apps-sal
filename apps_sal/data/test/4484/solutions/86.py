n, m = list(map(int, input().split()))


def facmod(a, mod):
    res = 1
    for i in range(1, a+1):
        res = (res*i) % mod
    return res


mod = 10**9+7
mn = min(m, n)
mx = max(m, n)
if abs(mn-mx) > 1:
    ans = 0
else:
    if n == m:
        ans = (2*facmod(m, mod)*facmod(n, mod)) % mod
    else:
        ans = (facmod(mx, mod)*facmod(mn, mod)) % mod
print(ans)

