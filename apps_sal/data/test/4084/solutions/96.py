n, a, b = map(int, input().split())
s = n // (a+b)
r = n % (a+b)

if r <= a:
    print(s*a + r)
elif r > a:
    print(s*a + a)
