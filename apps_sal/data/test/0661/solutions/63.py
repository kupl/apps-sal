M, K = map(int, input().split())

if K >= 2**M:
    print(-1)
    return
elif M == 0:
    print("0 0")
elif M == 1:
    if K == 0:
        print("0 0 1 1")
    else:
        print(-1)
else:
    A = [i for i in range(2**M) if i != K]
    B = A[::-1]

    for a in A:
        print(a, end=" ")
    print(K, end=" ")
    for b in B:
        print(b, end=" ")
    print(K)
