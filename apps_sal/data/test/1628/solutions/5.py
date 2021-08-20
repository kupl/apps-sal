(x, y) = list(map(input().count, 'xy'))
if x > y:
    print((x - y) * 'x')
else:
    print((y - x) * 'y')
