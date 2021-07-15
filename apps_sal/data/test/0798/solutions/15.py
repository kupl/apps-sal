a, b, c = map(int, input().split())
x = a
y = b
z = c
g = 0
if a > b + c or b > a + c or c > a + b or (a + b + c) % 2 != 0:
    print('Impossible')
    return 
if a >= b and a >= c:
    while x != y + z:
        g += 1
        y -= 1
        z -= 1
    print(y, g, z)
    return
if b >= a and b >= c:
    while y != x + z:
        g += 1
        x -= 1
        z -= 1
    print(x, z, g)
    return
if c >= a and c >= b:
    while z != x + y:
        g += 1
        x -= 1
        y -= 1
    print(g, y, x) 
