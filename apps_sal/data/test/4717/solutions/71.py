x, a, b = map(int, input().split())
if (x - a) ** 2 < (x - b) ** 2:
    print('A')
else:
    print('B')
