n,m,k=map(int,input().split())
l=list(map(int,input().split()))
ans=11**11
for i in range(n):
    if i==m-1 or l[i]>k or l[i]==0: continue
    if abs(m-1-i)<ans: ans=abs(m-1-i)
print(ans*10)
