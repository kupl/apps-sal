from collections import defaultdict
(n, W) = list(map(int, input().split()))
dd = defaultdict(list)
for i in range(n):
    (weight, value) = list(map(int, input().split()))
    dd[weight].append(value)
a = min(dd.keys())
(b, c, d) = (a + 1, a + 2, a + 3)
Vcum = defaultdict(lambda: [0])
for k in [a, b, c, d]:
    s = 0
    dd[k].sort(reverse=True)
    for val in dd[k]:
        s += val
        Vcum[k].append(s)
ans = 0
for w in range(len(dd[a]) + 1):
    for x in range(len(dd[b]) + 1):
        for y in range(len(dd[c]) + 1):
            for z in range(len(dd[d]) + 1):
                if W < a * w + b * x + c * y + d * z:
                    continue
                val = Vcum[a][w] + Vcum[b][x] + Vcum[c][y] + Vcum[d][z]
                ans = max(ans, val)
print(ans)
