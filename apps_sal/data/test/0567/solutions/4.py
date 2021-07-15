n=int(input())
el=map(int,input().split())
ans=0
for x in el:
    ans=max(ans,min(x-1,1000000-x))
print(ans)
