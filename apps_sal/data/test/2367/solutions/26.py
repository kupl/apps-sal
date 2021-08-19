(h, w, a, b) = list(map(int, input().split()))
p = 10 ** 9 + 7


def modp_factorial(n):
    s = 1
    for x in range(1, h + 1):
        s = s * x % p
    return s


def modp_prod(lst):
    s = 1
    for x in lst:
        s = s * x % p
    return s


def inv(n):
    s = 1
    q = p - 2
    while q > 0:
        if q & 1:
            s = s * n % p
        n = n * n % p
        q >>= 1
    return s


l = [1]
f = 1
for x in range(1, h + w):
    f = f * x % p
    l.append(f)
invl = [inv(l[-1])]
for n in range(h + w - 1, 1, -1):
    invl.append(invl[-1] * n % p)
invl.append(1)
invl.reverse()
s = 0
for x in range(1, h - a + 1):
    s = (s + modp_prod([l[x + b - 2], invl[x - 1], invl[b - 1], l[w - b + h - x - 1], invl[h - x], invl[w - b - 1]])) % p
print(s)
