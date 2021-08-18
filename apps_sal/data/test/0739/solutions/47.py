import math
import itertools

L, A, B, mod = [int(_) for _ in input().split()]


def sum_ri(r, n, mod):
    if r == 1:
        return n % mod
    else:
        return (pow(r, n, mod * (r - 1)) - 1) // (r - 1) % mod


def sum_iri(r, n, mod):
    if r == 1:
        return n * (n - 1) // 2 % mod
    else:
        r1 = r - 1
        p = pow(r, n, mod * r1**2)
        ret = (n - 1) * p * r1 + r1 - (p - 1)
        ret //= r1**2
        ret %= mod
        return ret


ans = 0

for digit in range(1, 20):
    ileft = max(0, (10**(digit - 1) - A - 1) // B + 1)
    iright = min(L - 1, (10**digit - A - 1) // B)
    if L <= ileft:
        break
    if ileft > iright:
        continue
    idiff = iright - ileft + 1
    pow10digit = pow(10, digit, mod)
    now = (A + B * iright) * sum_ri(pow10digit, idiff, mod)
    now -= B * sum_iri(pow10digit, idiff, mod)
    ans *= pow(10, digit * idiff, mod)
    ans += now
    ans %= mod
print(ans)
