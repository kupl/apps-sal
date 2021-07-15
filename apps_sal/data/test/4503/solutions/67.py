h,n=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=a[i]
if ans>=h:
    print("Yes")
else:
    print("No")
