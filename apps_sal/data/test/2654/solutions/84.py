def solve():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort(reverse=True)
    if N % 2 == 1:
        b = A[N // 2]
        u = B[N // 2]
        return u - b + 1
    b1 = A[N // 2 - 1]
    b2 = A[N // 2]
    u1 = B[N // 2 - 1]
    u2 = B[N // 2]
    return u1 + u2 - b1 - b2 + 1


print(solve())
