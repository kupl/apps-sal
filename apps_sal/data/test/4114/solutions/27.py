n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

for _ in range(0,n):
    if ab[_][2] !=0:
        x = ab[_][0]
        y = ab[_][1]
        h = ab[_][2]
        break

for i in range(101):
    for j in range(101):
        f = True
        l = abs(i-x)+abs(j-y)+h
        for k in range(0,n):
            dx = ab[k][0]
            dy = ab[k][1]
            dh = ab[k][2]
            if max(l-abs(i-dx)-abs(j-dy),0) ==dh:
                pass
            else:
                f = False
        if f:
            ansx =i
            ansy =j
            ansr = l
            break
print(str(ansx)+" "+str(ansy)+" "+str(ansr))
