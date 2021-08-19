(x, a, b) = map(int, input().split())
A = abs(a - x)
B = abs(b - x)
if A < B:
    print('A')
else:
    print('B')
