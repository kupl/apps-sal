n, b = map(int, input().split())
ans = 0
d = 2
bf = b
factors = []
while d * d <= b:
    if b % d == 0:
        cnt = 0
        while b % d == 0:
            cnt += 1
            b = b // d
        factors.append((d, cnt))
    d += 1

if b > 1:
    factors.append((b, 1))


def calc(x, y):
    yst = y
    ans = 0
    while yst <= x:
        ans += x // yst
        yst *= y
    return ans


ln = len(factors)
ans = min(calc(n, p[0]) // p[1] for p in factors)
print(ans)
