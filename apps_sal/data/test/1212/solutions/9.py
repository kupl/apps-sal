n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[a[0]]
for i in range(1,n):
    b.append(b[i-1]+a[i])
mina=b[k-1]
x=k-1
for i in range(k,n):
    if b[i]-b[i-k]<mina:
        x=i
        mina=b[i]-b[i-k]
print(x-k+2)
