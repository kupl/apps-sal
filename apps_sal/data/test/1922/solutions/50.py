N, M = map(int, input().split())
if (N == 2 or M == 2) or N * M == 2:
    print(0)
else:
    N = N - 2 if N > 2 else 1
    M = M - 2 if M > 2 else 1
    print(N * M)
