a, b, c = [int(x) for x in input().split(' ')]

d = [a,b,c]
d.sort()

dist = 0
mindis = d[2] + 1

for i in range(d[0], d[2] + 1):
    dist = abs(i - d[0]) + abs(i - d[1]) + abs(i - d[2])
    if dist < mindis: mindis = dist

print(mindis)
