n=int(input())
red=[[] for i in range(n)]
blue=[[] for i in range(n)]
for i in range(n):
    a,b=list(map(int,input().split()))
    red[i].append(a)
    red[i].append(b)
for i in range(n):
    a,b=list(map(int,input().split()))
    blue[i].append(a)
    blue[i].append(b)
red=sorted(red)
blue=sorted(blue)
ans=0
for i in range(n):
    x=blue[i][0]
    y=blue[i][1]
    maxy=-1
    for j in range(n):
        if x>red[j][0] and y>red[j][1]:
            maxy=max(maxy,red[j][1])
    for j in range(n):
        if x>red[j][0] and maxy==red[j][1]:
            ans+=1
            red[j][0]=1000
            break
print(ans)

