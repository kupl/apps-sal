n = int(input().strip())
s = str(input().strip())
x, y = list(map(int, input().strip().split()))
sumx = []
sumy = []

sx = 0
sy = 0
sumx.append(sx)
sumy.append(sy)
for i in s:
    if(i == 'U'):
        sy += 1
    elif(i == 'D'):
        sy -= 1
    elif(i == 'R'):
        sx += 1
    elif(i == 'L'):
        sx -= 1
    sumx.append(sx)
    sumy.append(sy)

#print("sxy",sx, sy)


def check(mid):
    i = 0
    while(i + mid <= n):
        dx = sumx[i + mid] - sumx[i]
        dy = sumy[i + mid] - sumy[i]
        cx = sx - dx
        cy = sy - dy
        # print("cxy",cx,cy)
        gdx = x - cx
        gdy = y - cy
        t = abs(gdx) + abs(gdy)
        # print("t",t)
        if(t % 2 == mid % 2 and t <= mid):
            return True
        i += 1
    return False


hi = n
lo = 0
mid = (hi + lo) // 2
while(hi - lo > 1):
    mid = (hi + lo) // 2
    #print("mid", mid)
    if(check(mid)):
        hi = mid
    else:
        lo = mid
# print(lo)
if(check(lo)):
    print(lo)
elif(check(mid)):
    print(mid)
elif(check(hi)):
    print(hi)
else:
    print(-1)
