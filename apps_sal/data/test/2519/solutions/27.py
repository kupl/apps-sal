N, K = map(int, input().split())
p = list(map(int, input().split()))
sum1 = 0.0
for i in range(K):
    sum1 = ((p[i] + 1) / 2.0) + sum1
sum2 = sum1
for i in range(N - K):
    sum1 = sum1 + ((p[i + K] - p[i]) / 2.0)
    if sum1 > sum2:
        sum2 = sum1
print(sum2)
