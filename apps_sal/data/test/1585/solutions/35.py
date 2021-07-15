x,y=map(int,input().split())

cnt=0

while(True):
    if x<=y:
        cnt+=1
        x=x*2
    else:
        print(cnt)
        return
