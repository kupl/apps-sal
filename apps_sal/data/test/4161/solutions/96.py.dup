def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(a, k + 1):
        for c in range(b, k + 1):
            d = gcd(a, b)
            if len({a, b, c}) == 1:
                ans += gcd(c, d)
            elif len({a, b, c}) == 2:
                ans += 3 * gcd(c, d)
            else:
                ans += 6 * gcd(c, d)
print(ans)
