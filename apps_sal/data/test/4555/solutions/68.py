(A, B, K) = map(int, input().split())
if K * 2 > B - A:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, A + K):
        print(i)
    for j in range(B - K + 1, B + 1):
        print(j)
