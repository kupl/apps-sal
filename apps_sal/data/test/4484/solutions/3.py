(N, M) = list(map(int, input().split()))
mod = 1000000007
if abs(N - M) > 1:
    print(0)
elif (N + M) % 2 == 1:
    x = max(N, M)
    y = min(N, M)
    Sum = 1
    for i in range(N + M):
        if i % 2 == 0:
            Sum *= x - i // 2
            Sum %= mod
        else:
            Sum *= y - i // 2
            Sum %= mod
    print(Sum)
else:
    Sum = 1
    for i in range(2 * N):
        Sum *= N - i // 2
        Sum %= mod
    Sum *= 2
    Sum %= mod
    print(Sum)
