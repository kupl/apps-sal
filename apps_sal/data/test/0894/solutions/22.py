x,y=list(map(int,input().split()))
m=abs(x)+abs(y)
if x>=0 :
    if y>=0:
        print(0,m,m,0)
    else:
        print(0,-m,m,0)
else :
    if y>=0:
        print(-m,0,0,m)
    else:
        print(-m,0,0,-m)
    

