N, K, x, y = [int(input()) for i in range(4)]

if K < N:
    print((N - K) * y + K * x)

else:
    print(N * x)
