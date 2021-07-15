n=int(input())
a=list(map(int,input().split()))
value=False
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            value=not value
b=[]
m=int(input())
for i in range(m):
    l,r=map(int,input().split())
    if ((r-l+1)//2)%2!=0:
        value=not value
    if value:
        b.append("odd")
    else:
        b.append("even")
print("\n".join(b))
