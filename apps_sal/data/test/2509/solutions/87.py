(N, K) = list(map(int, input().split()))
t = 0
for b in range(K + 1, N + 1):
    t += -~N // b * (b - K) + max(-~N % b - K, 0)
print(t - (0 if K else N - K))
