(a, b, c, k) = map(int, input().split())
ans = 0
while k:
    if a > 0 and k > 0:
        if a <= k:
            ans += a
            k -= a
            a = 0
        elif a > k:
            ans += k
            k = 0
            a -= k
    if b > 0 and k > 0:
        if b <= k:
            k -= b
            b = 0
        elif b > k:
            k = 0
            b -= k
    if c > 0 and k > 0:
        if c <= k:
            ans -= c
            k -= c
            c = 0
        elif c > k:
            ans -= k
            c -= k
            k = 0
print(ans)
