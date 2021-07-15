N, K, X, Y = [int(input()) for i in range(4)]
print(K * X + (N - K) * Y if N > K else N * X)
