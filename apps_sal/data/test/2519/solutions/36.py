(N, K) = map(int, input().split())
P = list(map(int, input().split()))
range_total = sum(P[:K]) + K
max_value = range_total
for i in range(N - K):
    range_total += P[K + i] - P[i]
    max_value = max(max_value, range_total)
print(max_value / 2)
