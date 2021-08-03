import sys
input = sys.stdin.readline
bsc = {}


def digs(x):
    s = 0
    while x > 0:
        s += 1
        x //= 10
    return s


def tenp(x):
    t = 1
    for i in range(x):
        t *= 10
    return t


def blocksize(b):
    if b in bsc:
        return bsc[b]
    d = digs(b)
    tp = tenp(d - 1)
    sz = d * (b - tp + 1)
    while d > 1:
        d -= 1
        tp //= 10
        sz += d * tp * 9
    bsc[b] = sz
    return sz


def dec(x):
    l = []
    while x > 0:
        l.append(x % 10)
        x //= 10
    return l[::-1]


def dig_in_block(mx, k):
    i, d, nd = 1, 1, 10
    while True:
        if d >= k:
            return dec(i)[k - 1]
        k -= d
        i += 1
        if i == nd:
            d += 1
            nd *= 10


def dig(k):
    b = 0
    while True:
        b += 1
        nsz = blocksize(b)
        if nsz >= k:
            break
        k -= nsz
    return dig_in_block(b, k)


q = int(input())
for _ in range(q):
    k = int(input())
    print(dig(k))
