N, K = map(int, input().split())
P = list(map(int, input().split()))

# 累積和
s = [0] * (N + 1)
for i in range(N):  # O(N)
    s[i + 1] = s[i] + P[i]

# [j,j+K) の和の最大値と j を保持
m = 0
midx = 0
for j in range(N - K + 1):  # O(N)
    v = s[j + K] - s[j]
    if v > m:
        m = v
        midx = j

E = 0
for k in range(midx, midx + K):  # O(K)
    x = P[k]
    E += (1 / x) * (x * (x + 1) / 2)
print(E)
