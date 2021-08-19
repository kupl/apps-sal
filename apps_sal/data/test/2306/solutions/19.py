n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
T = sum(t)
vmax_l = [0 for _ in range(2 * T + 1)]
vmax_r = [0 for _ in range(2 * T + 1)]
vmax = [0 for _ in range(2 * T + 1)]
for i in range(1, 2 * T + 1):
    tt = 0
    for j in range(n):
        if i > tt + t[j] * 2:
            tt += t[j] * 2
        else:
            vmax_l[i] = min(v[j], vmax_l[i - 1] + 0.5)
            break
for i in range(2 * T - 1, -1, -1):
    tt = 2 * T
    for j in range(n - 1, -1, -1):
        if i < tt - t[j] * 2:
            tt -= t[j] * 2
        else:
            vmax_r[i] = min(v[j], vmax_r[i + 1] + 0.5)
            break
for i in range(2 * T + 1):
    vmax[i] = min(vmax_l[i], vmax_r[i])
point_t = [0]
point_v = [0]
for i in range(1, 2 * T):
    if vmax[i - 1] != vmax[i] or vmax[i] != vmax[i + 1]:
        point_t.append(i)
        point_v.append(vmax[i])
point_t.append(2 * T)
point_v.append(0)
ans = 0
for i in range(1, len(point_t)):
    ans += (point_t[i] - point_t[i - 1]) * (point_v[i] + point_v[i - 1]) / 4
print(ans)
