(x, a, b) = map(int, input().split())
A = abs(x - a)
B = abs(x - b)
if A < B:
    print('A')
else:
    print('B')
