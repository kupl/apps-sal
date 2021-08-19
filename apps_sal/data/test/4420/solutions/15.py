for _ in range(int(input())):
    (x, y, n) = list(map(int, input().split()))
    z = n // x
    p = n % x
    if p >= y:
        print(z * x + y)
    else:
        print((z - 1) * x + y)
