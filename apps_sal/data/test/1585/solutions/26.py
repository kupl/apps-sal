x,y=map(int,input().split())

cnt=1
while x*2<=y:
    x*=2
    cnt+=1
print(cnt)
