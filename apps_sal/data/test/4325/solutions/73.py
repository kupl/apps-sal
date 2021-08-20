(n, x, t) = [int(num) for num in input().split()]
if n % x == 0:
    c = n // x
    print(c * t)
else:
    c = n // x
    print((c + 1) * t)
