xa,ya = map(int,input().split())
xb,yb = map(int,input().split())
xc,yc = map(int,input().split())
ans = []
xl = xb - xa
xs = yb - ya
a = abs(xl)
b = abs(xs)
x,y = xa,ya
dis = [[xa,ya],abs(xa-xc) + abs(ya-yc)]
for i in range(abs(xl) + abs(xs)):
    if a > 0 and b > 0:
        x1,y1 = x + xl//abs(xl),y
        d1 = abs(x1-xc) + abs(y1 - yc)
        x2,y2 = x, y + xs//abs(xs)
        d2 = abs(x2-xc) + abs(y2 - yc)
        if d1 < d2:
            ans.append([x,y])
            x,y = x1,y1
            a = a - 1
            if d1 < dis[1]:
                dis = [[x,y],d1]
        else:
            ans.append([x,y])
            b = b - 1
            x,y = x2,y2
            if d2 < dis[1]:
                dis = [[x,y],d2]
    elif a > 0:
        x1,y1 = x + xl//abs(xl),y
        d1 = abs(x1-xc) + abs(y1 - yc)
        ans.append([x,y])
        x,y = x1,y1
        a = a - 1
        if d1 < dis[1]:
            dis = [[x,y],d1]
    else:
        x2,y2 = x, y + xs//abs(xs)
        d2 = abs(x2-xc) + abs(y2 - yc)
        ans.append([x,y])
        b = b - 1
        x,y = x2,y2
        if d2 < dis[1]:
            dis = [[x,y],d2]        
ans.append([x,y])
xxl = xc - dis[0][0]
xxs = yc - dis[0][1]
a = abs(xxl)
b = abs(xxs)
x,y = dis[0][0],dis[0][1]
for i in range(abs(xxl) + abs(xxs)):
    if a > 0:
        x,y = x + xxl//abs(xxl),y
        a = a- 1
        ans.append([x,y])
    else:
        x,y = x,y + xxs//abs(xxs)
        b = b - 1
        ans.append([x,y]) 
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
