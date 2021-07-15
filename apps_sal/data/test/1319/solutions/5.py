from collections import Counter

MOD = 1000000007

def pow_m(base, pw):
    if pw == 0:
        return 1
    elif pw % 2 == 1:
        return (((pow_m(base, pw // 2) ** 2) % MOD) * base) % MOD
    else:
        return (pow_m(base, pw // 2) ** 2) % MOD

m = int(input())
p = [int(x) for x in input().split()]
c = Counter(p)

is_square = all(c[x] % 2 == 0 for x in c)

base, root, pw = 1, 1, 1
for elem in c:
    if is_square:
        ppw = pow_m(elem, c[elem] // 2)
        base = (base * ((ppw ** 2) % MOD)) % MOD
        root = (root * ppw) % MOD
    else:
        base = (base * pow_m(elem, c[elem])) % MOD
    pw *= c[elem] + 1
pw = (pw // 2) % (MOD - 1)

prod = pow_m(base, pw)
if is_square:
    prod = (prod * root) % MOD
print(prod)

