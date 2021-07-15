n,k=int(input()),int(input())
ans=1
i=0
while i!=n:
    if ans>=k:
        ans+=k
    else:
        ans*=2
    i+=1
print(ans)
