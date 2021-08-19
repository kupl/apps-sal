N, M = list(map(int, input().split()))

if N % 2 == 1:
    for i in range(1, M + 1):
        print(i, N - i)
else:
    # N=8 M=3 (8,1), (4,6), (7,2)
    # N=10, M=4 (10,1), (5,7), (9,2), (4,8)
    for i in range(M):
        if i % 2 == 0:
            x = i // 2
            print(N - x, 1 + x)
        else:
            cent = N // 2 + 1
            x = i // 2 + 1
            print(cent - x, cent + x)
