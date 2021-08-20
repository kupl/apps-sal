import re
o = input
C = len
E = float
F = int
d = print
U = sum
S = re.findall
l = o()
e = S('[\\d\\.]+', l)


def p(u):
    u = u.split('.')
    if C(u[-1]) == 2 and C(u) > 1:
        G = u[-1]
        return E(''.join(u[:-1]) + '.' + G)
    else:
        return F(''.join(u))


def V(flo):
    if F(flo) == flo:
        return '{:,}'.format(F(flo)).replace(',', '.')
    else:
        return '{:,.2f}'.format(flo).replace(',', '.')


e = [p(num) for num in e]
d(V(U(e)))
