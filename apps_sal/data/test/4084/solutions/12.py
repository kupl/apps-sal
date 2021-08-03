n, a, b = map(int, input().split())

ans = 0

b1 = n // (a + b) * a

if n % (a + b) >= a:
    print(b1 + a)
else:
    b2 = n % (a + b)
    print(b1 + b2)
