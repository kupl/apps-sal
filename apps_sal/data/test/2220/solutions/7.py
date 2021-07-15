n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
count=m//(k+1)
ans=arr[-1]*count*k
ans+=(arr[-2])*count
ans+=arr[-1]*(m%(k+1))
print(ans)
