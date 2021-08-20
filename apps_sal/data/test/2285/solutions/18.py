def zr(s):
    tmp = ':0000'
    if s == '::':
        return tmp[1:] + 7 * tmp
    ind = s.find('::')
    if ind < 0:
        return s
    (h, k) = (1, 0)
    if ind == 0 or ind == len(s) - 2:
        if ind > 0:
            h = 2
        else:
            k = 1
        ddc = 9 - s.count(':')
    else:
        ddc = 8 - s.count(':')
    return (s[:ind] + ddc * tmp + s[ind + h:])[k:]


def t4(s):
    ls = len(s)
    if ls == 4:
        return s
    return (4 - ls) * '0' + s


def spu(s):
    ns = ''
    fc = 0
    sc = s.find(':')
    while sc > 0:
        ns += t4(s[fc:sc]) + ':'
        fc = sc + 1
        sc = s.find(':', fc)
    ns += t4(s[fc:])
    return ns


n = int(input())
v = []
for c in range(n):
    v.append(spu(zr(input())))
for c in v:
    print(c)
