radius, width = input().split()
radius, width = int(radius), int(width)

sausages = int(input())
count = 0

for _ in range(sausages):
    x, y, r = input().split()
    x, y, r = int(x), int(y), int(r)

    dist = (x**2 + y**2)**0.5

    if ((dist - r) >= radius - width) and ((dist + r) <= radius):
        count += 1

print(count)
