(N, M) = list(map(int, input().split()))
if N % 2 == 1:
    for i in range(1, M + 1):
        print(i, N - i)
else:
    for i in range(M):
        if i % 2 == 0:
            x = i // 2
            print(N - x, 1 + x)
        else:
            cent = N // 2 + 1
            x = i // 2 + 1
            print(cent - x, cent + x)
