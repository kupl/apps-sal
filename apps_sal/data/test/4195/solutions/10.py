(d, n) = map(int, input().split())
if d == 0:
    if n != 100:
        print(n)
    else:
        print(101)
elif d == 1:
    if n != 100:
        print(n * 100)
    else:
        print(10100)
elif d == 2:
    if n != 100:
        print(n * 10000)
    else:
        print(1010000)
