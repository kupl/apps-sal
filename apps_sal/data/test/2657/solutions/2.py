N=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)
half=a[0]/2
ans1=a[0]
flag=10**9+10

for i in range(1,N):
    if flag>abs(a[i]-half):
        ans2=a[i]
        flag=abs(a[i]-half)

print(ans1,ans2)
