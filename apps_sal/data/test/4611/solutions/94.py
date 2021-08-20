N = int(input())
plan = []
Feasible = True
for i in range(N):
    (t, x, y) = map(int, input().split())
    plan.append([t, x, y])
(t0, x0, y0) = (0, 0, 0)
for (t1, x1, y1) in plan:
    dx = x1 - x0
    dy = y1 - y0
    dt = t1 - t0
    dist = abs(dx) + abs(dy)
    d = dt - dist
    if dt < dist:
        Feasible = False
    elif (dist + dt) % 2 != 0:
        Feasible = False
    (t0, x0, y0) = (t1, x1, y1)
print('Yes' if Feasible else 'No')
