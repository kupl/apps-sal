N = int(input())
xyh = [list(map(int,input().split())) for n in range(N)]
xyh.sort(key=lambda x:x[2],reverse=True)#高度１でない情報から高さ定めるため
for X in range(0,101):
    for Y in range(0,101):
        H = xyh[0][2] + abs(xyh[0][0]-X) + abs(xyh[0][1]-Y)
        for i in range(1,N):
            x,y,h = xyh[i]
            if h != max(H - abs(x-X) -abs(y-Y),0):
                break
        else:
            print(X,Y,H)
            break
