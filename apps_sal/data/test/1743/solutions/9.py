n=int(input())
a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
c=list(map(int,input().strip().split()))
d1,d2=a[0],b[0]
for i in range(1,n):
    d1,d2=max(d1+b[i],d2+a[i]),max(d1+c[i],d2+b[i])
print (d1)
