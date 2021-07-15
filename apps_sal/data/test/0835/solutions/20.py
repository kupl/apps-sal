def scan(type):
    return list(map(type, input().split()))

string, = scan(str)
nb,ns,nc = scan(int)
pb,ps,pc = scan(int)
r, = scan(int)

b = s = c = 0
for char in string:
    if (char == 'B'): b += 1
    if (char == 'S'): s += 1
    if (char == 'C'): c += 1

ans = 0

if (b == 0):
    nb = 0
if (s == 0):
    ns = 0
if (c == 0):
    nc = 0

while (True):
    if (b):
        qb = nb//b
    else:
        qb = 100

    if (s):
        qs = ns//s
    else:
        qs = 100

    if (c):
        qc = nc//c
    else:
        qc = 100

    qmin = min(qb,qs)
    qmin = min(qmin,qc)

    ans += qmin

    nb -= qmin*b
    ns -= qmin*s
    nc -= qmin*c
    
    if (nb == 0 and ns == 0 and nc == 0):
        break

    if (nb < b):
        r -= pb * (b-nb)
        nb = b

    if (ns < s):
        r -= ps * (s-ns)
        ns = s

    if (nc < c):
        r -= pc * (c-nc)
        nc = c
    
    if (r < 0):
        break

if (r > 0):
    cost = b*pb + s*ps + c*pc
    ans += r//cost

print(ans)


# 1482779206983

