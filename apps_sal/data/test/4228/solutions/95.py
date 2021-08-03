N, L = list(map(int, input().split()))

A = [i for i in range(L, L + N)]

if A[0] < 0:
    if A[-1] < 0:
        print((sum(A) - max(A)))
    else:
        print((sum(A)))
else:
    print((sum(A) - min(A)))
