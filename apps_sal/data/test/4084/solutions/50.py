n, a, b = map(int, input().split())
 
if a == 0:
    print(0)
    return
 
syou = n // (a+b)
amari = n % (a+b)
 
if amari <= a:
    print(syou*a + amari)
else:
    print(syou*a + a)
