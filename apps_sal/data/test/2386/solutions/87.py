n=int(input())
*a,=map(int,input().split())
b=sorted([x-i for i,x in enumerate(a)])
ans=0
for x in b:
    ans+=abs(x-b[n//2])

print(ans)
