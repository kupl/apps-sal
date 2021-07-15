with open(0) as f:
    x, a, b = map(int, f.read().split())
print('A' if abs(x-a) < abs(x-b) else 'B')
