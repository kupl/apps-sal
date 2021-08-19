(m, b) = list(map(int, input().split()))
maxS = 0
for (x, y) in zip(list(range(0, (b + 1) * m, m)), list(range(b, -1, -1))):
    vert = int((1 + y) * y / 2)
    hor = int((1 + x) * x / 2)
    newS = vert * (x + 1) + hor * (y + 1)
    if newS > maxS:
        maxS = newS
print(maxS)
