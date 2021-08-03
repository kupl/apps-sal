k = 72
K = 1 << k
def nu(L): return int("".join([bin(K + a)[-k:] for a in L[::-1]]), 2)
def st(n): return bin(n)[2:] + "0"
def li(s, l): return [int(a, 2) if len(a) else 0 for a in [s[-(i + 1) * k - 1:-i * k - 1] for i in range(l)]]


def grow(d, v, h):
    h += [0] * d
    f = [(-1 if (i + d) % 2 else 1) * fainv[i] * fainv[d - i] % P * h[i] % P for i in range(d + 1)]

    for idx, a in enumerate([d + 1, d * fa[v - 1] * fainv[v] % P, (d * fa[v - 1] * fainv[v] + d + 1) % P]):
        t = [1] * (2 * d + 2)
        for i in range(1, 2 * d + 2):
            t[i] = t[i - 1] * (a - d + i - 1) % P
        ti = [1] * (2 * d + 2)
        ti[-1] = pow(t[-1], P - 2, P)
        for i in range(1, 2 * d + 2)[::-1]:
            ti[i - 1] = ti[i] * (a - d + i - 1) % P

        g = [ti[i + 1] * t[i] % P for i in range(2 * d + 1)]
        fg = li(st(nu(f) * nu(g)), d * 2 + 2)

        if idx == 1:
            for i in range(d + 1):
                h[i] = h[i] * (fg[d + i] * t[d + i + 1] % P * ti[i] % P) % P
        elif idx == 0:
            for i in range(d):
                h[i + d + 1] = fg[d + i] * t[d + i + 1] % P * ti[i] % P
        elif idx == 2:
            for i in range(d):
                h[i + d + 1] = h[i + d + 1] * (fg[d + i] * t[d + i + 1] % P * ti[i] % P) % P
    return h

# Create a table of the factorial of the first v+2 multiples of v, i.e., [0!, v!, 2v!, ..., (v(v+1))!]


def create_table(v):
    s = 1
    X = [1, v + 1]
    while s < v:
        X = grow(s, v, X)
        s *= 2
    table = [1]
    for x in X:
        table.append(table[-1] * x % P)
    return table


def fact(i, table):
    a = table[i // v]
    for j in range(i // v * v + 1, i + 1):
        a = a * j % P
    return a


P = 10**9 + 7
v = 1 << 11
fa = [1] * (2 * v + 2)
fainv = [1] * (2 * v + 2)
for i in range(2 * v + 1):
    fa[i + 1] = fa[i] * (i + 1) % P
fainv[-1] = pow(fa[-1], P - 2, P)
for i in range(2 * v + 1)[::-1]:
    fainv[i] = fainv[i + 1] * (i + 1) % P

T = create_table(v)


def f(a, b): return fact(a + b + 2, T) * pow(fact(a + 1, T) * fact(b + 1, T), P - 2, P) % P


r1, c1, r2, c2 = list(map(int, input().split()))
print(((f(r2, c2) - f(r2, c1 - 1) - f(r1 - 1, c2) + f(r1 - 1, c1 - 1)) % P))
