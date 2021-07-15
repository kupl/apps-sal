X, Y = list(map(int, input().split()))

if (X == 0 and Y == 0) or (X == 0 and Y == 1) or (
        X == 1 and Y == 0) or (X == 1 and Y == 1):
    print('Brown')
    return

num = abs(X - Y)

if num <= 1:
    print('Brown')
else:
    print('Alice')

