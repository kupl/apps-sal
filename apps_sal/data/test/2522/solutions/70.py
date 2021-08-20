def solve(N, A, B):
    buf = -1
    key = 0
    for i in range(N):
        if buf != A[i]:
            key = 0
        if A[i] == B[i]:
            for j in range(key, N):
                if A[i] != A[j] and B[j] != A[i]:
                    (B[i], B[j]) = (B[j], B[i])
                    key = j
                    break
            else:
                print('No')
                return
        buf = A[i]
    print('Yes')
    print(' '.join([str(i) for i in B]))


def __starting_point():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, A, B)


__starting_point()
