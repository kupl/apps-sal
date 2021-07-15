n,a,b,c, = map(int,input().split())
l = list(int(input()) for i in range(n))
ans = 10 ** 6
for i in range(4 ** n):
    m = i
    j = 0
    x,xp,y,yp,z,zp = 0,0,0,0,0,0
    while m > 0:
        p = m % 4
        if p == 1:
            x += l[j]
            xp += 1
        elif p == 2:
            y += l[j]
            yp += 1
        elif p == 3:
            z += l[j]
            zp += 1
        else:
            pass
        m = m // 4
        j += 1
    if xp != 0 and yp != 0 and zp != 0:
        t = abs(a-x) + abs(b-y) + abs(c-z) + ((xp-1)*10) + ((yp-1)*10) + ((zp-1)*10)
        ans = min(ans,t)
print(ans)
