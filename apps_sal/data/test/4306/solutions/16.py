with open(0) as f:
    a, b, c, d = map(int, f.read().split())
f = lambda x: 0 if x < 0 else x
print(f(min(b, d) - max(a, c)))
