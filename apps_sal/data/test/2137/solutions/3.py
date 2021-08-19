(n, a, b) = map(int, input().split())
ghosts = [(vx, vy) for (x, vx, vy) in (map(int, input().split()) for i in range(n))]
speeds = {}
for (vx, vy) in ghosts:
    vl = a * vx - vy
    k = vx + a * vy
    ss = speeds.setdefault(vl, {})
    ss[k] = ss.get(k, 0) + 1
result = 0
for (vl, ss) in speeds.items():
    group_size = sum(ss.values())
    for sss in ss.values():
        result += sss * (group_size - sss)
print(result)
