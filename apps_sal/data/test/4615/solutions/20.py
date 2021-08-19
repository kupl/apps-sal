(A, B, C, D, E, F) = map(int, input().split(' '))
water = set()
for a in range(0, F, 100 * A):
    for b in range(0, F, 100 * B):
        if a + b <= F:
            water.add(a + b)
        else:
            break
sugars = set()
for c in range(0, F, C):
    for d in range(0, F, D):
        if c + d <= F:
            sugars.add(c + d)
        else:
            break
density = 0
sugar = 0
content = 100 * A
for x in water:
    for y in sugars:
        if x + y != 0 and x + y <= F and (E * x >= 100 * y) and (density < y / (x + y)):
            density = y / (x + y)
            sugar = y
            content = x + y
print(content, sugar)
