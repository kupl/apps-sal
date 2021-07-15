n, m = [int(i) for i in input().split()]

while n != 0 and m != 0:
    if n >= 2 * m:
        k = n // (2 * m)
        n -= 2 * m * k
    elif m >= 2 * n:
        k = m // (2 * n)
        m -= 2 * n * k
    else:
        break
print(n, m)
