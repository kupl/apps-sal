l, a, b, m = list(map(int, input().split()))


def c111(n, l, m):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 1:
        return (c111(n - 1, l, m) * pow(10, l, m) + 1) % m
    half = c111(n // 2, l, m)
    return (half * pow(10, (n // 2) * l, m) + half) % m


def c123(n, l, m):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 1:
        return (c123(n - 1, l, m) + c111(n, l, m)) % m
    half = c123(n // 2, l, m)
    return (half * pow(10, (n // 2) * l, m) + half + (n // 2) * c111(n // 2, l, m)) % m


fst, lst = a, a + b * (l - 1)

fst_l, lst_l = len(str(fst)), len(str(lst))

res, margin = 0, 0
for keta in reversed(list(range(fst_l, lst_l + 1))):
    num_l = a + b * ((10 ** (keta - 1) - a + b - 1) // b)
    num_r = a + b * ((10 ** keta - a + b - 1) // b - 1)
    if keta == fst_l:
        num_l = fst
    if keta == lst_l:
        num_r = lst
    if num_l > num_r:
        continue
    sz = (num_r - num_l) // b + 1
    _111 = num_l * c111(sz, keta, m)
    _123 = b * c123(sz - 1, keta, m)
    res += (pow(10, margin, m) * (_111 + _123)) % m
    margin += sz * keta
print((res % m))
