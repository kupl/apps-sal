n=int(input())
ans=0
l=[list(map(int,input().split())) for i in range(3)]
for i in range(1,n+1):
    ans+=l[1][l[0][i-1]-1]
    if i!=n and l[0][i]==l[0][i-1]+1:
        ans+=l[2][l[0][i-1]-1]
print(ans)
