N, D = map(int, input().split())
M = 2 * D + 1
if N % M == 0:
    print(N // M)
else:
    print(N // M + 1)
