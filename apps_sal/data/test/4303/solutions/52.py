n,k = map(int,input().split())
x = list(map(int,input().split()))
ans = 10 ** 12
for i in range(n-k+1):
    ans = min(ans,abs(x[i])+(abs(x[i+k-1]-x[i])),abs(x[i+k-1])+(abs(x[i+k-1]-x[i])))
print(ans)
