n = int(input())
AB = list((list(map(int, input().split())) for _ in range(n)))
CD = list((list(map(int, input().split())) for _ in range(n)))
CD.sort()
AB.sort(key=lambda z: z[1], reverse=True)
dim_b = [[] for _ in range(n)]
for b in range(n):
    (bx, by) = CD[b]
    for r in range(n):
        (rx, ry) = AB[r]
        if rx < bx and ry < by:
            dim_b[b] += [r]
vis_r = [False] * n
for b in range(n):
    max_ry = max_r = -1
    for r in dim_b[b]:
        if vis_r[r]:
            continue
        (rx, ry) = AB[r]
        if max_ry < ry:
            max_ry = ry
            max_r = r
    if max_r >= 0:
        vis_r[max_r] = True
print(sum(vis_r))
