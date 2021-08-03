n, a, b = list(map(int, input().split()))
c = n // (a + b)
if a < n % (a + b):
    print((c * a + a))
else:
    print((c * a + n % (a + b)))
