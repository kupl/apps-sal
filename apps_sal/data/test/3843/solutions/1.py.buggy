def D(n):
    x, r = n - 1, 1
    while x >= 7:
        x //= 7
        r += 1
    return r


def H(n, l):
    x, r = n, ""
    if x == 0:
        r += '0'
    while x:
        r += chr(ord('0') + x % 7)
        x //= 7
    r += '0' * (l - len(r))
    return r


a, b = list(map(int, input().split()))
la = D(a)
lb = D(b)
V = [0] * 99
r = 0


def F(deep, wa, wb):
    nonlocal r
    if wa >= a or wb >= b:
        return
    if deep == la + lb:
        r += 1
        return
    i = -1
    while i < 6:
        i += 1
        if V[i]:
            continue
        V[i] = 1
        if deep >= la:
            F(deep + 1, wa, wb + i * (7**(lb - 1 - (deep - la))))
        else:
            F(deep + 1, wa + i * (7**(la - 1 - deep)), wb)
        V[i] = 0


if la + lb < 8:
    F(0, 0, 0)
print(r)
