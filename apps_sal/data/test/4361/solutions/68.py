N, K, *H = list(map(int, open(0).read().split()))
H.sort()
print((min(H[i + K - 1] - H[i] for i in range(N - K + 1))))
