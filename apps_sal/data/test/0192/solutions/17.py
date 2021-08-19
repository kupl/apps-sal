line1 = input().split()
x = int(line1[0])
y = int(line1[1])
(a, b, c) = (y, y, y)
steps = 0
while a < x or b < x or c < x:
    a = b + c - 1
    steps += 1
    (a, b, c) = (min(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), max(a, b, c))
print(steps)
