(N, K) = list(map(int, input().split()))
P = [(int(x) + 1) / 2 for x in input().split()]
total = ans = sum(P[:K])
for n in range(K, N):
    total += P[n] - P[n - K]
    ans = max(ans, total)
print(ans)
