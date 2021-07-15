n=int(input())
ans=1
for b in range(2,100):
    tmp=b
    for p in range(2,10):
        tmp*=b
        if tmp<=n :
            ans=max(ans,tmp)
print(ans)
