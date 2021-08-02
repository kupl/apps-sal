N, M = [int(i) for i in input().split()]
if N % 2 == 1:
    for i in range(1, M + 1):
        print(i, end=" ")
        print(N + 1 - i)
    return
L = min(M, N // 4)
for i in range(1, L + 1):
    print(i, end=" ")
    print(N + 1 - i)
if L < M:
    for i in range(L + 1, M + 1):
        print(i, end=" ")
        print(N - i)
