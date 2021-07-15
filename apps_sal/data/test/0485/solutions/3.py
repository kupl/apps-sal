n = int(input())

l = []
dx = dict()
dy = dict()

for _ in range(4 * n + 1):
    x, y = list(map(int, input().split(" ")))
    l.append((x, y))
    dx[x] = dx.get(x, 0) + 1
    dy[y] = dy.get(y, 0) + 1

xmin = min(dx.keys())
xmax = max(dx.keys())
ymin = min(dy.keys())
ymax = max(dy.keys())

def find(enu, f):
    for e in enu:
        if f(e):
            return e
    return None

intruder = None
if dx[xmin] == 1:
    intruder = find(l, lambda e: e[0] == xmin)
elif dx[xmax] == 1:
    intruder = find(l, lambda e: e[0] == xmax)
elif dy[ymin] == 1:
    intruder = find(l, lambda e: e[1] == ymin)
elif dy[ymax] == 1:
    intruder = find(l, lambda e: e[1] == ymax)
else:
    intruder = find(l, lambda e: e[0] > xmin and e[0] < xmax and e[1] > ymin and e[1] < ymax)

x, y = intruder
print(x, y)

