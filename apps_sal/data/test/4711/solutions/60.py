with open(0) as f:
    (a, b, c) = map(int, f.read().split())
print(a + b + c - max(a, b, c))
