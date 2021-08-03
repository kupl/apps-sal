n, k = map(int, input().split())
mn = n // k
print(1 if n // k * k != n else 0)
