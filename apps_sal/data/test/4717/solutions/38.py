(x, a, b) = list(map(int, input().split()))
if abs(x - a) < abs(x - b):
    print('A')
else:
    print('B')
