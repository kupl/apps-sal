x,y=map(int,input().split())
ans=x
cnt=0
while ans<=y:
    ans*=2
    cnt+=1
print(cnt)
