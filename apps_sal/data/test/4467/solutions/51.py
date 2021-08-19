n = int(input())
AB = list(list(map(int, input().split())) for _ in range(n))
CD = list(list(map(int, input().split())) for _ in range(n))

# print(*CD,sep='\n',end='\n---\n')
# print(*sorted(CD, key=lambda x: x[0]),sep='\n',end='\n---\n')
# CD.sort(key=lambda x: x[1])
# CD.sort(key=lambda x: x[0])
CD.sort()
# print(*CD,sep='\n',end='\n---\n')
# print(*AB,sep='\n',end='\n---\n')
AB.sort(key=lambda x: x[1], reverse=True)
# print(*AB,sep='\n',end='\n---\n')

dim_r = [[] for _ in range(n)]
dim_b = [[] for _ in range(n)]
# cnt_r = [0]*n
# cnt_b = [0]*n
for b in range(n):
    bx, by = CD[b]
    for r in range(n):
        rx, ry = AB[r]
        if rx < bx and ry < by:
            dim_r[r] += [b]
            dim_b[b] += [r]
            # cnt_b[b] += 1
            # cnt_r[r] += 1

# print(n)
# print(*AB,sep='\n',end='\n---\n')
# print(*CD,sep='\n',end='\n---\n')
# print(*dim_r,sep='\n',end='\n---\n')
# print(*dim_b,sep='\n',end='\n---\n')
# # print(cnt_b,end='\n---\n')

ans = 0

inf = 1000000000
vis_r = [False] * (n)
for b in range(n):
    bx, by = CD[b]
    # print('b,bx,by',b,bx,by)
    max_ry = -1
    max_r = -1
    for r in dim_b[b]:
        if vis_r[r]:
            continue
        # print('r,rx,ry',r,rx,ry)
        rx, ry = AB[r]
        if max_ry < ry:
            max_ry = ry
            max_r = r
    if max_r >= 0:
        # print('max_r,max_ry',max_r,max_ry)
        vis_r[max_r] = True
        ans += 1
    # print('---')
print(ans)
