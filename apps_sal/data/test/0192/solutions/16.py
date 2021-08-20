(x, y) = map(int, input().split())
counter = 0
(x, y) = (min(x, y), max(x, y))
x1 = x
x2 = x
x3 = x
while y > x1 or y > x2 or y > x3:
    if x1 != y:
        x1 = min(x3 + x2 - 1, y)
        counter += 1
    if x2 != y:
        x2 = min(x1 + x3 - 1, y)
        counter += 1
    if x3 != y:
        x3 = min(x1 + x2 - 1, y)
        counter += 1
print(counter)
