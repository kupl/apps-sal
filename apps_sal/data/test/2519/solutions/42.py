(N, K) = map(int, input().split())
p = list(map(int, input().split()))
for i in range(N):
    p[i] = p[i] / 2 + 0.5
s = 0
for i in range(K):
    s += p[i]
maxSum = s
j = 0
for i in range(K, N):
    s = s + p[i] - p[i - K]
    maxSum = max(maxSum, s)
print(maxSum)
