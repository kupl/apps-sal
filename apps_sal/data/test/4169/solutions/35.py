a,b=map(int,input().split())
c=[list(map(int,input().split())) for i in range(a)]

c=sorted(c,key=lambda x:x[0])
ans=0
for i in range(a):
    if b==0:
        break
    elif b>=c[i][1]:
        b-=c[i][1]
        ans+=c[i][1]*c[i][0]
    else:
        ans+=b*c[i][0]
        break
print(ans)
