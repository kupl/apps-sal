N, K = map(int, input().split())
ans = N % K
ans = min(ans, abs(ans - K))
print(ans)
