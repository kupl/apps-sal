n=int(input())
a=list(map(int,input().split()))[::-1]
if n!=1:
    summax,summin=max(a[0],a[1]),min(a[0],a[1])
else:
    summin=0;summax=a[0]
for i in range(2,n):
    if summax<summin + a[i]:
        summax,summin=summin + a[i],summax
    else:
        summin=summin+a[i]
print(summin,summax)
