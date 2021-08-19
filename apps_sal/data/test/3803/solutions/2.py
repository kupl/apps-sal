(hy, ay, dy) = map(int, input().split())
(hm, am, dm) = map(int, input().split())
(h, a, d) = map(int, input().split())
s = 1 << 30
for da in range(max(0, dm - ay + 1), max(0, hm - ay + dm) + 1):
    for dd in range(max(0, am - dy) + 1):
        dh = max(0, (am - dy - dd) * ((hm - 1) // (ay + da - dm) + 1) - hy + 1)
        s = min(s, h * dh + a * da + d * dd)
print(s)
