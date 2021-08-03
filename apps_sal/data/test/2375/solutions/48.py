X, Y = map(int, input().split())

if X >= Y + 2:
    print('Alice')
elif X <= Y - 2:
    print('Alice')
else:
    print('Brown')
