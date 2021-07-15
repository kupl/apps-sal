(n, m) = list(map(int, input().split()))

while (n != 0 and m != 0) or (n >= 2 * m) or (m >= 2 * n):
    if n == 0:
        break
    elif m == 0:
        break
    elif n >= 2 * m:
        n = n % (2 * m)
    elif m >= 2 * n:
        m = m % (2 * n)
    else:
        break

print(n, m)

