h, w, x, y, z, p = list(map(int, input().split()))
x, y, z = x % 4, y % 2, z % 4

def rotation(a, b):
    nonlocal h, w
    res = (b, h - a + 1)
    w, h = h, w
    return res

def flip(a, b):
    return a, w - b + 1

res = []
for i in range(p):
    a, b = list(map(int, input().split()))
    ch, cw = h, w
    for i in range(x):
        a, b = rotation(a, b)
    for i in range(y):
        a, b = flip(a, b)
    for i in range(3 * z):
        a, b = rotation(a, b)
    res += [str(a) + ' ' +  str(b)]
    h, w = ch, cw

print('\n'.join(map(str, res)))

