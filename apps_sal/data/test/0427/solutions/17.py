a, b, c, d = map(int, input().split())
l = 1
r = 10**10
while r - l > 1:
    m = (r + l) // 2
    both = m // (c * d)
    f = [m // c, m // d]
    other = m - f[0] - f[1] + both
    f[0] -= both
    f[1] -= both
    if max(0, b - f[0]) + max(0, a - f[1]) <= other:
        r = m
    else:
        l = m
print(r)
