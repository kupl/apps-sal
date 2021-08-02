n = int(input()) - 1
r = 0
while n != 0:
    zz = 1
    a = 1
    z = 1
    while zz <= n:
        z <<= 1
        zz <<= 1
        zz += 1
        a <<= 1
        a += z
    zz >>= 1
    a -= z
    a >>= 1
    n -= zz
    r += a
    if n:
        n -= 1
        r += z
print(r)
