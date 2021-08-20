(a, b) = map(int, input().split())
x = (a + b) / 2
if x.is_integer():
    print(int(x))
else:
    print('IMPOSSIBLE')
