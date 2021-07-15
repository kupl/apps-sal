n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(n):
    if a[i]<0:
        count+=1
if count%2==0:
    for j in range(n):
        a[j]=abs(a[j])
    print((sum(a)))
else:
    for j in range(n):
        a[j]=abs(a[j])
    print((sum(a)-2*min(a)))
    

