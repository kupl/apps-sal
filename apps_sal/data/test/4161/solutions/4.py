K = int(input())
ans = 0


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        d = gcd(a, b)
        for c in range(1, K + 1):
            ans += gcd(c, d)

print(ans)
