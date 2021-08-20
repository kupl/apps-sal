(x, y) = map(int, input().split())
L = list(range(2, 14)) + [1]
a = L.index(x)
b = L.index(y)
if a > b:
    print('Alice')
elif b > a:
    print('Bob')
else:
    print('Draw')
