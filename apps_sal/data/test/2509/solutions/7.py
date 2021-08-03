N, K = list(map(int, input().split()))

t = 0
for b in range(K + 1, N + 1):
    t += (N // b) * (b - K) + ((N % b - K + (1 if K > 0 else 0) if N % b >= K else 0)if N % b else 0)
print(t)
