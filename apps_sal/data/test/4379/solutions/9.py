n=int(input())
d=dict()
m=0
val=0
a=list(map(int,input().split()))
s=set()
aps=s.add
for i in a:
    d[i]=d.get(i-1,0)+1
    if d[i]>m:
        m=d[i]
        val=int(i)

ans=[]
ap=ans.append
for i in range(n-1,-1,-1):
    if a[i]==val:
        val-=1
        ap(i+1)
print(m)
print(*ans[::-1])
