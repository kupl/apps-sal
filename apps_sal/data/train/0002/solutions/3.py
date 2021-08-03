T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]
    B = [int(_) for _ in input().split()]
    C = [int(_) for _ in input().split()]

    R = []

    for i in range(N):
        if i == 0:
            R.append(A[i])
            continue
        if i == N - 1:
            if A[i] != R[0] and A[i] != R[-1]:
                R.append(A[i])
            elif B[i] != R[0] and B[i] != R[-1]:
                R.append(B[i])
            else:
                R.append(C[i])
            continue

        if A[i] != R[-1]:
            R.append(A[i])
        else:
            R.append(B[i])

    print(' '.join(map(str, R)))
