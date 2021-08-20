(n, a, b) = list(map(int, input().split()))
x = n % (a + b)
y = n // (a + b)
if x > a:
    print(a * (y + 1))
else:
    print(a * y + x)
