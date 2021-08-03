n, a, b = map(int, input().split())

p = n // (a + b)
q = n % (a + b)
if q <= a:
    amari = q
else:
    amari = a

if a == 0:
    print(0)
elif q <= a:
    print(a * p + amari)
else:
    print(a * p + amari)
