def pow2(c, d):
    if d == 0:
        return 1
    if d == 1:
        return c
    return pow2(c, d // 2) ** 2 * c ** (d % 2) % INF


INF = 10 ** 9 + 7
(a, b, n, x) = list(map(int, input().split()))
if a != 1:
    SGP = (b - b * pow2(a, n)) * pow2(1 - a, INF - 2) % INF
else:
    SGP = b * n
print((SGP + pow2(a, n) * x) % INF)
