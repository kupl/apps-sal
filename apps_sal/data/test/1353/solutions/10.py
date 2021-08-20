(n, m, a, b) = map(int, input().split())
if b / m >= a:
    print(a * n)
elif n // m * b + n % m * a < (n // m + 1) * b:
    print(n // m * b + n % m * a)
else:
    print((n // m + 1) * b)
