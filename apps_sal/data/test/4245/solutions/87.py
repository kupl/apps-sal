(a, b) = map(int, input().split())
print((b - 1) // (a - 1) + (1 if (b - 1) % (a - 1) != 0 else 0))
