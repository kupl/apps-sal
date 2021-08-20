from math import ceil
(D, G) = map(int, input().split())
(ps, cs) = ([], [])
for _ in range(D):
    (p, c) = map(int, input().split())
    ps.append(p)
    cs.append(c)
ans = float('inf')
for i in range(2 ** D):
    cnt = 0
    point = 0
    for j in range(D):
        if i >> j & 1:
            cnt += ps[j]
            point += ps[j] * 100 * (j + 1) + cs[j]
    if point >= G:
        ans = min(ans, cnt)
        continue
    for j in range(D - 1, -1, -1):
        if i >> j & 1 == 0:
            if (ps[j] - 1) * 100 * (j + 1) + point >= G:
                cnt += ceil((G - point) / 100 / (j + 1))
                point += ceil((G - point) / 100 / (j + 1)) * 100 * (j + 1)
                break
            else:
                cnt += ps[j] - 1
                point += (ps[j] - 1) * 100 * (j + 1)
    if point >= G:
        ans = min(ans, cnt)
print(ans)
