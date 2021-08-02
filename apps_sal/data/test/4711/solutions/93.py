a, b, c = map(int, input().split())

kei = a + b + c

if a >= b and a >= c:
    kei -= a
    print(kei)

elif b >= a and b >= c:
    kei -= b
    print(kei)
else:
    kei -= c
    print(kei)
