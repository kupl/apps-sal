(N, K) = map(int, input().split())
if K % 2 == 1:
    print((N // K) ** 3)
else:
    a = N // K
    t = K // 2
    b = (N - t) // K + 1
    print(a ** 3 + b ** 3)
