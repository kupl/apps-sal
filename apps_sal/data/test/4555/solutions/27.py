(A, B, K) = map(int, input().split())
for i in range(A, min(A + K, B + 1)):
    print(i)
for i in range(max(A + K, B - K + 1), B + 1):
    print(i)
