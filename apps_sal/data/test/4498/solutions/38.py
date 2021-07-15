a, b, c, d = map(int, input().split())
f = lambda x, y: abs(x - y) <= d
print('Yes' if (f(a, b) and f(b, c)) or f(a, c) else 'No')
