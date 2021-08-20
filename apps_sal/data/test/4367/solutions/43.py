(n, r) = map(int, input().split())
if n >= 10:
    print(r)
else:
    a = 100 * (10 - n)
    b = a + r
    print(b)
