N, K = map(int, input().split())
p = list(map(int, input().split()))
l = [sum(p[:K])]
for i in range(1, N - K + 1):
    l.append(l[-1] - p[i - 1] + p[i + K - 1])
print((max(l) + K) / 2)
