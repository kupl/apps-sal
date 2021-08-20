import math
(n, k) = map(int, input().split())
(x, y, c) = zip(*[map(int, input().split()) for _ in range(n)])
que = [(0, 0, 1000)]
res = 1000000000.0
i = 0
while i < len(que):
    (px, py, r) = que[i]
    i += 1
    lb = [c[j] * math.hypot(max(abs(px - x[j]) - r, 0), max(abs(py - y[j]) - r, 0)) for j in range(n)]
    if res * (1 - 5e-07) > sorted(lb)[k - 1]:
        dis = [c[j] * math.hypot(px - x[j], py - y[j]) for j in range(n)]
        res = min(res, sorted(dis)[k - 1])
        for dx in (-0.5, 0.5):
            for dy in (-0.5, 0.5):
                que.append((px + dx * r, py + dy * r, r / 2))
print(res)
