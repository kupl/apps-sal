def p(f):
    r = 0
    for x in f:
        if x * a > b:
            r += b
        else:
            r += x * a
    return r


def scan(): return map(int, input().split())


a, b, c, d = scan()
n, m = scan()
f = list(scan())
g = list(scan())
r1 = p(f)
if r1 > c:
    r1 = c
r2 = p(g)
if r2 > c:
    r2 = c
r = r1 + r2
if r > d:
    r = d
print(r)
