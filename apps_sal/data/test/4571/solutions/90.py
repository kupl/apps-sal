n, m = map(int, input().split())

# ((n - m) * 100 + m * 1900) * 2^m

print(((n - m) * 100 + m * 1900) * pow(2, m))
