p1 = input().split()
p1 = [int(x) for x in p1]
p2 = input().split()
p2 = [int(x) for x in p2]
xmax, xmin, ymax, ymin = -1000, 1000, -1000, 1000
centrx, centry = sum([p2[i] for i in [0, 2, 4, 6]]) / 4, sum([p2[i] for i in [1, 3, 5, 7]]) / 4
r = abs(centrx - p2[0]) + abs(centry - p2[1])

for i in [0, 2, 4, 6]:
    xmax = max(xmax, p1[i])
    xmin = min(xmin, p1[i])
for i in [1, 3, 5, 7]:
    ymax = max(ymax, p1[i])
    ymin = min(ymin, p1[i])

def Inside(x, y):
    return x <= xmax and x >= xmin and y <= ymax and y >= ymin

ok = False

for i in range(-100, 101):
    for j in range(-100, 101):
        if abs(i - centrx) + abs(j - centry) <= r:
            ok = ok or Inside(i, j)

print(["NO\n", "YES\n"][int(ok)])
