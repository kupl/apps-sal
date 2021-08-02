X, Y = map(int, open(0).read().split())
if abs(X - Y) <= 1:
    print('Brown')
else:
    print('Alice')
