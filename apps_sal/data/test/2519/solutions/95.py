N, K = map(int, input().split())
P = list(map(int, input().split()))
ans = 0
for i in range(K):
    ans += (P[i] + 1) / 2

tmp = ans
for i in range(K, N):
    tmp = tmp + (P[i] + 1) / 2 - (P[i - K] + 1) / 2
    ans = max(ans, tmp)

print(ans)
