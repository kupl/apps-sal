(N, K) = map(int, input().split())
res = (N // K) ** 3
if K % 2 == 0:
    res += ((N - K // 2) // K + 1) ** 3
print(res)
