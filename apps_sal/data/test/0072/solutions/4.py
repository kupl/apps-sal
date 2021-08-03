s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
n = int(input())

a = input()
b = input()
c = input()

m = len(a)

x = max([a.count(r) for r in s])
y = max([b.count(r) for r in s])
z = max([c.count(r) for r in s])

if n == 1:
    if x == m:
        x -= 1
    else:
        x += 1
    if y == m:
        y -= 1
    else:
        y += 1
    if z == m:
        z -= 1
    else:
        z += 1
else:
    x = min(m, x + n)
    y = min(m, y + n)
    z = min(m, z + n)

mx = max(x, y, z)

if x == mx and y < mx and z < mx:
    print('Kuro')
elif x < mx and y == mx and z < mx:
    print('Shiro')
elif x < mx and y < mx and z == mx:
    print('Katie')
else:
    print('Draw')
