a, b, n = map(int, input().split())
print((a * min(n, b - 1)) // b - a * (min(n, b - 1) // b))
