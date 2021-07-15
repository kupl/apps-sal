N, K = map(int, input().split())
print((N // K) ** 3 if K % 2 == 1 else (((N // K) ** 3) + ((N - K // 2) // K + 1) ** 3))
