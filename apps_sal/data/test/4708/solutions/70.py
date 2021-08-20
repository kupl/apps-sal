(N, K, X, Y) = [int(input()) for i in range(4)]
if K >= N:
    Z = N * X
    print(Z)
else:
    Z = K * X + (N - K) * Y
    print(Z)
