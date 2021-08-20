(n, m) = [int(k) for k in input().split()]
minimum = min(m, n)
print(minimum + 1)
points = [(0, m)]
x = 0
y = m
done = False
while not done:
    x += 1
    y -= 1
    points.append((x, y))
    if x == n or y == 0:
        done = True
for i in points:
    print(str(i[0]) + ' ' + str(i[1]))
