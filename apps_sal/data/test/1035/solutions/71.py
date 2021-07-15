def factorize(n):
    fct = []
    b,e = 2,0
    while b*b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e > 0:
            fct.append((b,e))
        b,e = b+1,0
    if n > 1:
        fct.append((n,1))
    return fct
a,b = map(int,input().split())
ap = set()
for prime,count in factorize(a):
    ap.add(prime)
bp = set()
for prime,count in factorize(b):
    bp.add(prime)
print(len(ap&bp)+1)
