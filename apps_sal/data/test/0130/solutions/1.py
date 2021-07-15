n,m=list(map(int,input().split()))
blacksX,blacksY=[],[]
count=0
for x in range(n):
    inp=input()
    for y in range(m):
        if inp[y]=='B':
            blacksX.append(x)
            blacksY.append(y)
            count+=1
if len(blacksX)==0:
    print(1)
else:
    side=max(max(blacksX)-min(blacksX)+1,max(blacksY)-min(blacksY)+1)
    if side <=n and side <= m:
        print(side*side-count)
    else:
        print(-1)

