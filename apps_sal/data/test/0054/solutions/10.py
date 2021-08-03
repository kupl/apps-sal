W, M = (input().split(' '))
W = int(W)
M = int(M)

if W == 2 or W == 3:
    print("YES")
else:
    N = 16
    A = [0] * (N + 1)
    A[0] = 1
    for I in range(1, N):
        A[I] = A[I - 1] * W
        if A[I] > 10000000001000000000:
            N = I
            break
    # print(N)
    S = set()

    ok = False
    for msk in range(1 << N):
        curr = 0
        for I in range(N):
            if msk & (1 << I) > 0:
                curr += A[I]
        if curr == M or (curr - M in S):
            ok = True
            break
        S.add(curr)

    if ok:
        print("YES")
    else:
        print("NO")
