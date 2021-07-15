n=int(input())
a=list(map(int,input().split()))
s=sum(a)//2
x=s-sum(a[1::2])
table=[x]
for i in range(n-1):
    table.append(a[i]-x)
    x=a[i]-x
ans=list(map(lambda x:2*x,table))
print(*ans)
