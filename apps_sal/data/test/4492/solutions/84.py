N, K = map(int, input().split())
a = list(map(int, input().split()))
if a[0] > K:
    ans = a[0] - K
    a[0] = K
else:
    ans = 0
for i in range(1, N):
    if a[i - 1] + a[i] > K:
        ans += a[i] - (K - a[i - 1])
        a[i] = K - a[i - 1]
print(ans)
