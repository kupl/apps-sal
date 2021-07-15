N, K = list(map(int, input().split()))

ans = 0
if N % K == 0:
    ans = 0
else:
    a = N % K
    b = abs(a - K)
    ans = min(a, b)
print(ans)
