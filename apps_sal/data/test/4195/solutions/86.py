d, n = map(int, input().split())

if d == 0:
    if n == 100:
        print(101)
    else:
        print(n)
elif d == 1:
    if n == 100:
        print(10100)
    else:
        print(n * 100)
else:
    if n == 100:
        print(100**2 * 100 + 10000)
    else:
        print(100**2 * n)
