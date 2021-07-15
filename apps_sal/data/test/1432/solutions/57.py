n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
sum=0
for i in range(n-1):
    if i%2==0:
        sum-=a[i]
    else:
        sum+=a[i]
sum+=a[n-1]
ans[-1]=sum
for j in range(0,n-1)[::-1]:
    ans[j]+=(2*a[j]-ans[j+1])
for k in range(n):
    ans[k]=str(ans[k])
print((" ".join(ans)))

