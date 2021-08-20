(d, n) = map(int, input().split())
if n == 100:
    if d == 1:
        print(10100)
    elif d == 2:
        print(10000 * 101)
    else:
        print(101)
else:
    print(100 ** d * n)
