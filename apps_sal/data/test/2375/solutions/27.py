(X, Y) = map(int, input().split())
(X, Y) = (max(X, Y), min(X, Y))
if X <= 1:
    print('Brown')
elif X - Y >= 2:
    print('Alice')
else:
    print('Brown')
