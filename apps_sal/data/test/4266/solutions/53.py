(K, X) = map(int, input().split())
m = X - (K - 1)
for i in range(2 * K - 1):
    print(m + i, end=' ')
