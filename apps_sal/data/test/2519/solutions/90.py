N, K = map(int, input().split())
P = list(map(int, input().split()))

s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + P[i]

m = 0
midx = 0
for j in range(N - K + 1):
    v = s[j + K] - s[j]
    if v > m:
        m = v
        midx = j

E = 0
for k in range(midx, midx + K):
    x = P[k]
    E += (1 / x) * (x * (x + 1) / 2)
print(E)
