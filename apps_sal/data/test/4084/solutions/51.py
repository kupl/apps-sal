n, a, b = map(int, input().split())

q = n // (a + b)
r = n % (a + b)

if r >= a:
    res = a
else:
    res = r

print(q * a + res)
