N, K = map(int, input().split())
B = 1
R = N - K + 1

for k in range(K):
    print(B * R % (10**9 + 7))
    B = B * (K - k - 1) // (k + 1)
    R = R * (N - K - k) // (k + 2)
