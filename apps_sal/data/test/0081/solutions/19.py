def mp():
    return map(int, input().split())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


(a, b) = mp()
(a, b) = (min(a, b), max(a, b))
x = []
w = b - a
dl = 1
while dl ** 2 <= w:
    if w % dl == 0:
        x.append(dl)
        x.append(w // dl)
    dl += 1
kk = 0
m = 10 ** 20
for d in x:
    r = (a + d - 1) // d
    k = r * d - a
    if lcm(a + k, b + k) < m:
        m = lcm(a + k, b + k)
        kk = k
print(kk)
