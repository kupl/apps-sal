n = int(input())
AB = list((list(map(int, input().split())) for _ in range(n)))
CD = list((list(map(int, input().split())) for _ in range(n)))
CD.sort()
AB.sort(key=lambda z: z[1], reverse=True)
vis_r = [False] * n
for b in range(n):
    for r in range(n):
        if not vis_r[r] and AB[r][0] < CD[b][0] and (AB[r][1] < CD[b][1]):
            vis_r[r] = True
            break
print(sum(vis_r))
