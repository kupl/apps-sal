N, M = map(int, input().split())

if N == 1 and M == 1:
    print(1)
elif min(N, M) == 1:
    print(N + M - 3)
elif min(N, M) == 2:
    print(0)
else:
    print((N-2)*(M-2))
