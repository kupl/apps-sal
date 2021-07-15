n,m=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
cnt=0
for i in range(n):
    if a[i] >= s/(4*m):
        cnt += 1
if cnt>=m:
    print('Yes')
else:
    print('No')
