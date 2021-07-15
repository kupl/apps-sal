n = int(input())
AB = list(list(map(int,input().split())) for _ in range(n))
CD = list(list(map(int,input().split())) for _ in range(n))

CD.sort() # sort x in ascending order
AB.sort(key=lambda z: z[1], reverse=True) # sort x in descending order

dim_b = [[] for _ in range(n)]
for b in range(n):
    for r in range(n):
        if AB[r][0] < CD[b][0] and AB[r][1] < CD[b][1]:
            dim_b[b] += [r]

vis_r = [False]*(n)
for b in range(n): # ascending order of x
    for r in dim_b[b]: # descending order of y
        if not vis_r[r]: vis_r[r] = True; break

print((sum(vis_r)))

