(N, K) = map(int, input().split())
ans = N % K
if abs(ans - K) < ans:
    ans = abs(ans - K)
print(ans)
