n = int(input())
points = set()
starts = {}
ends = {}
for i in range(n):
    (a, b) = map(int, input().split())
    points.add(a)
    points.add(b)
    starts[a] = 1 + starts.get(a, 0)
    ends[b] = 1 + ends.get(b, 0)
spoints = sorted(points)
dwd = {}
prev_point = spoints[0]
density = 0
for (i, cur_point) in enumerate(spoints):
    interval_length = cur_point - prev_point - 1
    if interval_length > 0:
        dwd[density] = interval_length + dwd.get(density, 0)
    starts_here = starts.get(cur_point, 0)
    density += starts_here
    dwd[density] = 1 + dwd.get(density, 0)
    ends_here = ends.get(cur_point, 0)
    density -= ends_here
    prev_point = cur_point
for i in range(1, n + 1):
    print(dwd.get(i, 0), end=' ')
