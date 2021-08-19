(D, N) = list(map(int, input().split()))
D = 100 ** D
if N == 100:
    print(N * D + D)
else:
    print(N * D)
