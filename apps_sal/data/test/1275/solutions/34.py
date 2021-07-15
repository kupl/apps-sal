N,K=list(map(int,input().split()))
def f(N,K):
    ans = max(0,min(K-1,2*N+1-K))
    return ans
ans = 0

for x in range(2,2*N+1):
    ans += f(N,x)*f(N,x-K)

print(ans)

