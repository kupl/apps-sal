A, B, K = map(int, input().split())
if B - A <= 2 * (K - 1):
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, A + K):
        print(i)
    for j in range(B - K + 1, B + 1):
        print(j)
