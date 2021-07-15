n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
s=sum(a)
t=0
for i in range(n-1):
    b.append(t+a[i])
    t=b[i]
for i in range(n-1):
    c.append(abs(2*b[i]-s))
c.sort()
print(c[0])
