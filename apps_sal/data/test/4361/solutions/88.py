N, K, *H = map(int, open(0).read().split())
H.sort()
ans = float('inf')
for i in range(N - K + 1):
    ans =min(ans, H[i + K - 1] - H[i])
print(ans)
