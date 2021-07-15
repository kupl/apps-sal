l,a,b,m = map(int,input().split())

# c111 -> 1001001001みたいなやつを求める
# n : 塊の数
# l : 一つの塊(00..001)の長さ
# m : mod
# ex) n=3, l=2 -> 10101
def c111(n, l, m):
    if n <= 1:
        return 1
    if n % 2 == 1:
        return (c111(n - 1, l, m) * pow(10, l, m) + 1) % m
    half = c111(n // 2, l, m)
    return (half * pow(10, (n // 2) * l, m) + half) % m

# c123 -> 1002003004みたいなやつを求める
# n : 塊の数
# l : 一つの塊(00..001)の長さ
# m : mod
# ex) n=3, l=2 -> 10203
def c123(n, l, m):
    if n <= 1:
        return 1
    if n % 2 == 1:
        return (c123(n - 1, l, m) + c111(n, l, m)) % m
    half = c123(n // 2, l, m)
    return (half * pow(10, (n // 2) * l, m) + half + (n // 2) * c111(n // 2, l, m)) % m

fst = a
lst = a + b * (l - 1)

fst_l = len(str(fst))
lst_l = len(str(lst))

res = 0
margin = 0
for keta in reversed(range(fst_l, lst_l + 1)):
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
    if sz == 1:
        _123 = 0
    res += (pow(10, margin, m) * (_111 + _123)) % m
    margin += sz * keta
print(res % m)
