(A, B, K) = map(int, input().split())
for num in range(A, min(B + 1, A + K)):
    print(num)
for num in range(max(A + K, B - K + 1), B + 1):
    print(num)
