N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))

Point = M * N - sum(A)

if Point >= 0 and Point <= K:
    print(Point)
elif Point > K:
    print((-1))
else:
    print((0))
