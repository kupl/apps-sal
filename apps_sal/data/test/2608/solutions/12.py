def wb(n,m,flip=False):
    w = b = n*m // 2
    if n%2 == 1 and m %2 == 1:
        w += 1
    if flip:
        return b,w
    else:
        return w,b

t = int(input())
for tt in range(t):
    n,m = map(int, input().split())
    x1,y1,x2,y2 = map(int, input().split())
    x3,y3,x4,y4 = map(int, input().split())
    x5 = max(x1,x3)
    x6 = min(x2,x4)
    y5 = max(y1,y3)
    y6 = min(y2,y4)
    ov = False
    if x6-x5 >= 0 and y6-y5 >= 0:
        ov = True
    w,b = wb(n,m)
    wm,bm = wb(x2-x1+1, y2-y1+1, (x1+y1)%2==1)
    wd,bd = wb(x4-x3+1, y4-y3+1, (x3+y3)%2==1)
    if ov:
        wo,bo = wb(x6-x5+1, y6-y5+1, (x5+y5)%2==1)
    else:
        wo,bo = 0,0
    # print('w, b', w, b)
    # print('wm, bm', wm, bm)
    # print('wd, bd', wd, bd)
    # print('wo, bo', wo, bo)
    w = w+bm-wd-bo
    b = b-bm+wd+bo
    print(w,b)
