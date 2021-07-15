n,k,m=list(map(int, input().split()))
a=list(map(int, input().split()))
req=m*n-sum(a)
print((max(0,req) if req<=k else -1))

