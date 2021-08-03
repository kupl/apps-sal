N, K = list(map(int, input().split()))
p = list(map(int, input().split()))
sum = 0
v = []
for i in range(K):
    sum += p[i]
v.append(sum)
for i in range(K, N):
    sum += p[i]
    sum -= p[i - K]
    v.append(sum)
M = 0
for i in range(N + 1 - K):
    M = max(M, v[i])
print(((M + K) / 2))
