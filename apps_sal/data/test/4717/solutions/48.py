(x, a, b) = list(map(int, input().split()))
print('A' if max(x, a) - min(x, a) < max(x, b) - min(x, b) else 'B')
