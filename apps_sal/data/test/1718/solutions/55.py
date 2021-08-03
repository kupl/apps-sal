N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
if N <= K:
    ans = 1
else:
    x = K
    ans = 1
    while(x < N):
        ans += 1
        x += (K - 1)

print(ans)
