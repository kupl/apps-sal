n,k=list(map(int,input().split()))
s=input()
st=[set() for i in range(n+1)]
st[n].add(s)
c=1
k-=1
ans=0
for i in range(n,0,-1):
    for w in st[i]:
        for j in range(i):
            st[i-1].add(w[:j]+(w[j+1:] if j!=i-1 else ''))
    sz=len(st[i-1])
    if k<sz:
        ans+=(n-i+1)*k
        k=0
        break
    else:
        ans+=(n-i+1)*sz
        k-=sz
    #print(i,k,ans)
    if k<0:
        break
if k>0:
    print(-1)
else:
    print(ans)
#print(k,ans,st)

