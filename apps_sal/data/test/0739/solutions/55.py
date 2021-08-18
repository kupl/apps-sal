L, A, B, M = list(map(int, input().split()))

ten = 0


def pow_(x, t):
    if t == 0:
        return 1
    if t % 2 == 1:
        return (pow_(x, t - 1) * x) % M
    else:
        y = pow_(x, t // 2)
        return (y * y) % M


def f(l):
    if l == 0:
        return 0
    if l % 2 == 1:
        pl = l - 1
        x = f(pl)
        return x * ten + 1
    else:
        pl = l // 2
        x = f(pl)
        return x * pow_(ten, pl) + x


def g(l):
    if l == 0:
        return 0
    if l % 2 == 1:
        pl = l - 1
        x = g(pl)
        return x * ten + B * pl
    else:
        pl = l // 2
        x = g(pl)
        return x * pow_(ten, pl) + x + B * pl * f(pl)


last = A + B * (L - 1)
ans = 0
ten = 10
for _ in range(18):
    l = ten // 10
    r = ten - 1

    if last < l:
        ten *= 10
        continue
    if A > r:
        ten *= 10
        continue
    na = 0
    nl = 0

    if A >= l:
        na = A
    else:
        na = (l - A + B - 1) // B * B + A
        na = min(na, last)

    nlast = 0
    if last <= r:
        nlast = last
    else:
        nlast = (r - A) // B * B + A
    nl = (nlast - na) // B + 1

    ans *= pow_(ten, nl) % M
    ans += (na * f(nl)) % M
    ans += g(nl) % M
    ten *= 10

print((ans % M))
