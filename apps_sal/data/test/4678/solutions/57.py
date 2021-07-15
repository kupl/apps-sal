#abc176c
n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(1,n):
 d=max(a[i-1]-a[i],0)
 res+=d
 a[i]+=d
print(res)

