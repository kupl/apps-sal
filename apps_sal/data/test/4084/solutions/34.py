n, b, c = map(int, input().split())
c += b
print(n // c * b + min(b, n % c))
