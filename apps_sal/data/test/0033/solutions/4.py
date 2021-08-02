from fractions import gcd


def egcd(a, b):
    if a == 0:
        return [0, 1]
    if b == 0:
        return [1, 0]
    p = egcd(b % a, a)
    x = p[0]; y = p[1]
    return [y - x * (b // a), x]


def solve(a1, m1, a2, m2):
    sol = egcd(m1, m2)
    m1x = m1 * sol[0]
    m2y = m2 * sol[1]
    return (m1x * a2 + m2y * a1)


a1, b1, a2, b2, L, R = list(map(int, input().split(' ')))
L -= b1; R -= b1; b2 -= b1; b1 = 0;
g = gcd(a1, a2)
L = max(L, max(b1, b2))
if (b2 % g != 0 or L > R):
    print(0)
    quit()
rmod = a1 * a2 // g;
a1 //= g; b2 //= g; a2 //= g;
sol = solve(b1, a1, b2, a2);
mod = a1 * a2;
sol %= mod; sol *= g;
L -= sol; R -= sol;
if (L <= 0):
    lnew = L % rmod; R += lnew - L; L = lnew;
L += rmod; R += rmod;
print(R // rmod - (L - 1) // rmod)
