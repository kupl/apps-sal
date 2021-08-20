n = int(input())
pos = list(map(int, input().split()))
v = list(map(int, input().split()))
t0 = 0
t1 = max(1, (max(pos) - min(pos)) / 2)
while t1 - t0 > 1e-07:
    tmid = (t0 + t1) / 2
    inter = [pos[0] - v[0] * tmid, pos[0] + v[0] * tmid]
    va = 1
    for i in range(1, n):
        a = pos[i] - v[i] * tmid
        b = pos[i] + v[i] * tmid
        if a < inter[0] and b > inter[1]:
            continue
        if inter[0] <= a <= inter[1]:
            inter[0] = max(inter[0], a)
        if inter[0] <= b <= inter[1]:
            inter[1] = min(inter[1], b)
        if b < inter[0] or a > inter[1]:
            break
    else:
        va = 0
        t1 = tmid
    if va:
        t0 = tmid
print(tmid)
