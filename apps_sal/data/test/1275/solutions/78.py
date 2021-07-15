N, K = list(map(int, input().split()))

ans = 0
for i in range(2, 2*N+1):
    ans += min(i-1, 2*N-i+1) * max(0,min(i-K-1, 2*N-i+K+1))
print(ans)

