N, K, X, Y = [int(input()) for _ in range(4)]
print(X * min(K, N) + Y * max(0, N - K))
