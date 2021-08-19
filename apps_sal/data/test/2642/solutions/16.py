from math import gcd
n = int(input())
mod = 10 ** 9 + 7
d1 = dict()
d2 = dict()
zero = 0
zeroa = 0
zerob = 0
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    if a == 0 and b == 0:
        zero += 1
    elif a == 0 and b != 0:
        zeroa += 1
    elif a != 0 and b == 0:
        zerob += 1
    else:
        g = gcd(abs(a), abs(b))
        na = a // g
        nb = b // g
        if na < 0:
            na = -na
            nb = -nb
        if (na, nb) not in d1 and (na, nb) not in d2:
            d1[na, nb] = 1
            d2[-nb, na] = 0
            d2[nb, -na] = 0
        elif (na, nb) in d1:
            d1[na, nb] += 1
        else:
            d2[na, nb] += 1
d1 = list(d1.items())
ans = pow(2, zeroa, mod) + pow(2, zerob, mod) - 1
ans %= mod
for ((a, b), cnt1) in d1:
    cnt2 = 0
    cnt2 += d2[-b, a]
    cnt2 += d2[b, -a]
    ans *= pow(2, cnt1, mod) + pow(2, cnt2, mod) - 1
    ans %= mod
ans += zero
ans = (ans + mod - 1) % mod
print(ans)
