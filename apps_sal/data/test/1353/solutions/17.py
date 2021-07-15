n, m, a, b = list(map(int, input().split()))
if n > m:
    if b < a * m:
        print(min((n // m) * b + (n - ((n // m) * m)) * a, ((n // m) * b) + b))
    else:
        print(n * a)
else:
    print(min(b, n * a))

