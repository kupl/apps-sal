n, m = [int(x) for x in input().split()]
h1 = lambda k: 6 * ((k - 1) // 2) + 2 * ((k - 1) % 2 + 1) if k > 0 else 0
h2 = lambda k: 3 + (k - 1) * 6 if k > 0 else 0
h3 = lambda l: 6 * k
newx = lambda k: k - 2 if k % 6 == 4 else k - 4
newy = lambda k: k - 6
x, y, z = h1(n), h2(m), 0
while max(x, y) > z + 6:
    z += 6
    if x > y:
        x = newx(x)
    else:
        y = newy(y)
print(max(x, y, z))
