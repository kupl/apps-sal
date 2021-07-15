n=int(input())
a=[int(s) for s in input().split()]
a.append(-1)
k=1
prev=0
cn=0
ans=0
for i in range(1,n+1):
    if a[i]==a[i-1]:
        k+=1
    else:
        ans=max(ans,min(k,prev))
        prev=k
        k=1
print(ans*2)
