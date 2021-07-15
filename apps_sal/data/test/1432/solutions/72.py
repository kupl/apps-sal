n=int(input())
a=list(map(int,input().split()))
b=sum(a)
ans=[0]*n
for i in range(n//2):
    ans[(i+1)*2]=ans[i*2]-(2*(a[i*2]-a[i*2+1]))
ans[1]=ans[-1]-(2*(a[-1]-a[0]))
for i in range(1,n//2):
    ans[i*2+1]=ans[(i-1)*2+1]-(2*(a[(i-1)*2+1]-a[i*2]))
c=(b-sum(ans))//n
ans2=[0]*n
for i in range(n):
    ans2[i]=c+ans[i]
print((*ans2))

