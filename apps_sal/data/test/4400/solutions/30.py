S=input()
ans=0
cnt=0
for s in S:
    if s=="S":
        ans=max(ans,cnt)
        cnt=0
    else:
        cnt+=1
ans=max(ans,cnt)
print(ans)
