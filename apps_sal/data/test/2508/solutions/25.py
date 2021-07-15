h,w,k = map(int,input().split())
y1,x1,y2,x2 = map(int,input().split())
grid = []
grid.append(['@']*(w+2))
for i in range(h):
    grid.append(['@']+list(input())+['@'])
grid.append(['@']*(w+2))

q = set()
next_q = set()
next_q.add((y1,x1))
ans = 0
while True:
    if not next_q:
        print(-1)
        return
    for y,x in next_q:
        grid[y][x] = '@'
    q = next_q
    next_q = set()
    while q:
        y,x = q.pop()
        if (y,x) == (y2,x2):
            print(ans)
            return
        for i in range(1,k+1):
            if grid[y+i][x] == '@':
                break
            next_q.add((y+i,x))
        for i in range(1,k+1):
            if grid[y-i][x] == '@':
                break
            next_q.add((y-i,x))
        for i in range(1,k+1):
            if grid[y][x+i] == '@':
                break
            next_q.add((y,x+i))
        for i in range(1,k+1):
            if grid[y][x-i] == '@':
                break
            next_q.add((y,x-i))
    ans += 1
