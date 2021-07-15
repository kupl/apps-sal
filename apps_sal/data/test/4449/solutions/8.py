Q = int(input())
for q in range(Q):
    N = int(input())
    A = sorted([int(a) for a in input().split()])
    S = A[0] * A[-1]
    i, j = 0, 4*N-1
    for _ in range(N):
        if not(A[i] == A[i+1] and A[j] == A[j-1] and A[i] * A[j] == S):
            print("NO")
            break
        i += 2
        j -= 2
    else:
        print("YES")

