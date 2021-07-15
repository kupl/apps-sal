n,h=map(int,input().split())
ans=n
for x in list(map(int,input().split())):
    if x>h: ans+=1
print(ans)
