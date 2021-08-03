x, a, b = map(int, input().split())
A = abs(a - x)
B = abs(b - x)
print('A' if A < B else 'B')
