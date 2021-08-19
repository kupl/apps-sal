from collections import defaultdict, Counter
(H, W, N) = list(map(int, input().split()))
L = []
for _ in range(N):
    (a, b) = list(map(int, input().split()))
    L.append([a, b])
d = defaultdict()
for i in range(N):
    for sx in range(3):
        for sy in range(3):
            if 3 <= L[i][0] + sx <= H and 3 <= L[i][1] + sy <= W:
                if (L[i][0] + sx, L[i][1] + sy) not in d:
                    d[L[i][0] + sx, L[i][1] + sy] = 1
                else:
                    d[L[i][0] + sx, L[i][1] + sy] += 1
c = Counter(list(d.values()))
ans = [0 for _ in range(10)]
for (k, v) in list(c.items()):
    if v > 0:
        ans[k] = v
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])
for i in ans:
    print(i)
