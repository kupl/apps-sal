n, b, c = map(int, input().split())
print(n // (b + c) * b + min(b, n % (b + c)))
