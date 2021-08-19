(x, y) = map(int, input().split())
if x > y:
    (x, y) = (y, x)
if y - x <= 1:
    print('Brown')
else:
    print('Alice')
