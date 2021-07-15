k,n=map(int,input().split())
a=list(map(int,input().split()))

c=[]
for i in range(1,n):
    c.append(a[i]-a[i-1])
c.append(k-a[-1]+a[0])

print(k-max(c))
