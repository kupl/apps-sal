N = int(input())
A = list(map(int, input().split()))
if all((v >= 0 for v in A)):
    print(N - 1)
    for i in range(1, N):
        print((i, i + 1))
elif all((v < 0 for v in A)):
    print(N - 1)
    for i in reversed(list(range(1, N))):
        print((i + 1, i))
else:
    max_ind = A.index(max(A)) + 1
    min_ind = A.index(min(A)) + 1
    if abs(max(A)) >= abs(min(A)):
        print(2 * N - 1)
        for i in range(1, N + 1):
            print((max_ind, i))
        for i in range(1, N):
            print((i, i + 1))
    else:
        print(2 * N - 1)
        for i in range(1, N + 1):
            print((min_ind, i))
        for i in reversed(list(range(1, N))):
            print((i + 1, i))
