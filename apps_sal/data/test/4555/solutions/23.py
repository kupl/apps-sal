A, B, K = list(map(int, input().split()))

if B - A + 1 > 2 * K:
    for i in range(K):
        print((A + i))
    for j in range(K):
        print((B - K + j + 1))
else:
    for k in range(B - A + 1):
        print((A + k))
