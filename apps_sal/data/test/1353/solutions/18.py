
n, m, a, b = list(map(int, input().split()))

if b / m < a:
    print(n // m * b + min(n % m * a, b))
else:
    print(a * n)

