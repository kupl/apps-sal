def to_bin(a):
    out = []
    while a > 0:
        if a % 2 == 1:
            out.append(1)
        else:
            out.append(0)
        a //= 2
    while len(out) < 6:
        out.append(0)
    return out


def to_dec(a):
    c = 1
    out = 0
    for i in a:
        out += i * c
        c *= 2
    return out


a = int(input())
b = to_bin(a)
c = []
c.append(b[4])
c.append(b[1])
c.append(b[3])
c.append(b[2])
c.append(b[0])
c.append(b[5])
print(to_dec(c))
