(x, a, b) = map(int, input().split())
la = abs(a - x)
lb = abs(b - x)
print('A' if la < lb else 'B')
