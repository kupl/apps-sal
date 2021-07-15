n=int(input())
h=list(map(int,input().split()))[::-1]
ans=[0]*n
for i in range(n-1):
    if h[i]<=h[i+1]:
        ans[i+1]+=ans[i]+1
print(max(ans))
