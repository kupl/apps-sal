(n, m, k) = map(int, input().split())
kk1 = min(k - 1, n - k)
kk2 = n - kk1 - 1
mm = m - n
s1 = (kk1 + 1) ** 2
if s1 >= mm:
    res = 1 + int(mm ** 0.5)
else:
    res = 1 + (kk1 + 1)
    mmm = mm - s1
    a = 2 * (kk1 + 1)
    b = kk2 - kk1 - 1
    s2 = a * b + b * (b - 1) // 2
    if s2 >= mmm:
        res += int(-(2 * a - 1) / 2 + (((2 * a - 1) / 2) ** 2 + 2 * mmm) ** 0.5)
    else:
        mmmm = mmm - s2
        res += b + mmmm // n
print(res)
