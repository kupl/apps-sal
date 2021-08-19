(K, X) = map(int, input().split())
inc = X + K - 1
dec = X - K + 1
for i in range(dec, K + X):
    print(i, end=' ')
