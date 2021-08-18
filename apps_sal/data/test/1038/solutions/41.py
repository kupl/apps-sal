
a, b = list(map(int, input().split()))


def xor(a, b):
    x = a
    for i in range(a + 1, b + 1):
        x = x ^ i
    print(("xor:", x))


ia = len(bin(a)) - 2
ib = len(bin(b)) - 2


def px(b, ib):
    bbr = []
    ip = 1
    for i in range(ib):
        ip *= 2
        bc = (b // ip) * (ip // 2)
        bc += max((b % ip + 1) - (ip // 2), 0)
        bbr.append(bc)
    return bbr


aar = px(a - 1, ib)
bbr = px(b, ib)

c = [0] * ib
ip = 1
for i in range(ib):
    ip *= 2
    ci = bbr[i] - aar[i]
    c[i] = ci % 2

ip = 1
csum = 0
for i in range(ib):
    csum += c[i] * ip
    ip *= 2

print(csum)
