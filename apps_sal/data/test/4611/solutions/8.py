N = int(input())
t = 0
xy = [0,0]
ans = 'Yes'
for i in range(N):
    ti,xi,yi = map(int,input().split())
    dt = ti - t
    dx = abs(xi - xy[0])
    dy = abs(yi - xy[1])
    if dt < dx+dy:
        ans = 'No'
    elif dt%2 != (dx+dy)%2:
        ans = 'No'
    t = ti
    xy = [xi,yi]
print(ans)
