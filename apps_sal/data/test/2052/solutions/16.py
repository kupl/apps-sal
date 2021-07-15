n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a[:k])
b=[]
c=0
b.append(s)
for i in range(n-k-1):
    s=s-a[i]+a[i+k]
    b.append(s)
print(min(b))
