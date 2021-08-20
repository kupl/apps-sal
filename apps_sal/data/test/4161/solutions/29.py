k = int(input())
ans = 0


def gcd(a, b):
    if a % b == 0:
        return b
    c = a % b
    return gcd(b, c)


for l in range(1, k + 1):
    for m in range(l, k + 1):
        for n in range(m, k + 1):
            tmp1 = gcd(l, n)
            tmp2 = gcd(tmp1, m)
            if l == m == n:
                ans += tmp2
            elif l == m or m == n:
                ans += 3 * tmp2
            else:
                ans += 6 * tmp2
print(ans)
