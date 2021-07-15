p,y=map(int,input().split(' '))
f2=0
for i in range(y,max(p,y-301),-1):
    f=0
    for j in range(2,min(int(i**0.5)+1,p+1)):
        if i%j==0:
            f=1
            break
    if f==0:
        f2=1
        print(i)
        break
if f2==0:
    print(-1)
