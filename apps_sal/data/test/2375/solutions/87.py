(X, Y) = map(int, input().split())
diff = abs(X - Y)
if diff < 2:
    print('Brown')
else:
    print('Alice')
