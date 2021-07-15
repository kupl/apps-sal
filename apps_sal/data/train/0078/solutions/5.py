t = int(input())
for i in range(t):
    e,s = list(map(int, input().split()))
    f = []
    for h in range(e):
        f.append(input())
    now = 0
    mi = 0
    mi2 = []
    g = []
    for y in range(e):
        now = 0
        g = []
        for x in range(s):
            if(f[y][x]=="*"):
                now+=1
            else:
                g.append(x)
        if(now>mi):
            mi = now
            mi2 = []
            for k in range(len(g)):
                mi2.append(g[k])
        elif(now==mi):
            for k in range(len(g)):
                mi2.append(g[k])
    now = 0
    ma = 0
    d = True
    for y in range(s):
        now = 0
        for x in range(e):
            if(f[x][y]=="*"):
                now+=1
        if(now>ma):
            ma = now
            if(y in mi2):
                d = False
            else:
                d = True
        elif(now==ma):
            if(y in mi2):
                d = False
    if(d):
        print(e-mi+s-ma)
    else:
        print(e-mi+s-ma-1)

