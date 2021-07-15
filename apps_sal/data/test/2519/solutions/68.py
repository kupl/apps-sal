N, K = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]

a = sum(p[:K])
s = sum(p[:K])
for i in range(K, N):
    s += p[i] - p[i - K]
    a = max(a, s)

ans = (a + K) / 2
print(ans)
