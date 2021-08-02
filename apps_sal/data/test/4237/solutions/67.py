a, b, c, d = list(map(int, input().split()))


def mul_count(v, w, n):
    if v % n == 0:
        s = v // n
    else:
        s = v // n + 1
    e = w // n
    if s > e:
        return 0
    else:
        return e - s + 1


def koyaku(x, y):
    big = max(x, y)
    small = min(x, y)
    amari = big % small
    if amari == 0:
        return small
    else:
        return koyaku(small, amari)


c_mul = mul_count(a, b, c)
d_mul = mul_count(a, b, d)

cd_common = koyaku(c, d)
cd_mul = c * d // cd_common
common_mul = mul_count(a, b, cd_mul)
yobun = c_mul + d_mul - common_mul
print((b - a + 1 - yobun))
