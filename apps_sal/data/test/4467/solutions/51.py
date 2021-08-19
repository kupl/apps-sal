n = int(input())
AB = list((list(map(int, input().split())) for _ in range(n)))
CD = list((list(map(int, input().split())) for _ in range(n)))
CD.sort()
AB.sort(key=lambda x: x[1], reverse=True)
dim_r = [[] for _ in range(n)]
dim_b = [[] for _ in range(n)]
for b in range(n):
    (bx, by) = CD[b]
    for r in range(n):
        (rx, ry) = AB[r]
        if rx < bx and ry < by:
            dim_r[r] += [b]
            dim_b[b] += [r]
ans = 0
inf = 1000000000
vis_r = [False] * n
for b in range(n):
    (bx, by) = CD[b]
    max_ry = -1
    max_r = -1
    for r in dim_b[b]:
        if vis_r[r]:
            continue
        (rx, ry) = AB[r]
        if max_ry < ry:
            max_ry = ry
            max_r = r
    if max_r >= 0:
        vis_r[max_r] = True
        ans += 1
print(ans)
