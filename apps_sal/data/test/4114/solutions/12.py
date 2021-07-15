n=int(input())
info=[list(map(int,input().split())) for i in range(n)]
for cx in range(0,101):
    for cy in range(0,101):
        H=-10**20
        lim=10**20
        for l in info:
            x,y,h=l 
            if h==0:
                 lim=min(lim,abs(x-cx)+abs(y-cy))
                 
            else:
                if H!=-10**20 and H!=abs(x-cx)+abs(y-cy)+h :break
                H=abs(x-cx)+abs(y-cy)+h 
            if H>lim:break
        else:
            print(cx,cy,H);return
