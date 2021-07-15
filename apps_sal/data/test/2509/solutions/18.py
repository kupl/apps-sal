N, K = map(int, input().split())
ans = 0
for b in range(K+1,N+1):
    ans += (b-K)*(N//b)
    if N//b*b+K <= N:
        ans += N - (N//b*b+K) +1 
if K == 0:
    ans -= N
print(ans)
