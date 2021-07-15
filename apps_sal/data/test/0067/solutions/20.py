def f(a):
    if a > 0:
        return '+'
    if a == 0:
        return '0'
    return '-'

x, y, z = list(map(int, input().split()))
if z == 0:
    print(f(x - y))
elif f(x - y - z) != f(x - y + z):
    print('?')
else:
    print(f(x-y-z))
