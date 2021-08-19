def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    (a, b) = divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


p = [0, 45, 9045, 1395495, 189414495, 23939649495, 2893942449495, 339393974949495, 38939394344949495, 1000000000000000001]
nx = [0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889]
q = int(input())
for ut in range(q):
    lk = int(input())
    k = lk
    idx = 0
    for i in range(len(p) - 1):
        if p[i] <= k and p[i + 1] > k:
            idx = i
    idx = idx
    k -= 1
    k -= p[idx]
    a = idx + 1
    b = 2 * nx[idx] + idx + 1
    k = -2 * k
    d = isqrt(b * b - 4 * a * k)
    x1 = (-b + d) / (2.0 * a)
    x2 = (-b - d) / (2.0 * a)
    a1 = int(x1)
    z = lk - p[idx] - nx[idx] * a1 - a1 * (a1 + 1) // 2 * (idx + 1)
    cnt = 0
    ww = 1
    pow = 0
    pow = 1
    while (cnt + pow * ww) * 9 < z:
        cnt += pow * ww
        ww += 1
        pow *= 10
    sym_cnt = z - cnt * 9 - 1
    ok = pow + sym_cnt / ww
    s = str(ok)
    if z < 10:
        print(z)
    else:
        print(s[sym_cnt % ww])
