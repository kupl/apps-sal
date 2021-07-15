h,w,n = map(int, input().split())
memo = {}
dxy = [(0,1), (0,0), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
for i in range(n):
    a,b = map(int, input().split())
    for dx,dy in dxy:
        x,y = a+dx,b+dy
        if 1 < x < h and 1 < y < w:
            if (x,y) not in memo:
                memo[(x,y)] = 0
            memo[(x,y)] += 1

ans = [0 for i in range(10)]
for k,v in memo.items():
    ans[v] += 1
ans[0] = (h-2)*(w-2) - sum(ans)
[print(i) for i in ans]
