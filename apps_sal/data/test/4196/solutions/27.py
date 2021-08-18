
def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(N, A):
    L = [0] * N
    L[0] = A[0]
    for i in range(1, N):
        L[i] = gcd(A[i], L[i - 1])
    R = [0] * N
    R[-1] = A[-1]
    for i in range(1, N):
        R[-(i + 1)] = gcd(A[-(i + 1)], R[-i])
    ans = 0
    for i in range(N):
        if i == 0:
            ans = max(ans, R[i + 1])
        elif i == N - 1:
            ans = max(ans, L[i - 1])
        else:
            ans = max(ans, gcd(L[i - 1], R[i + 1]))
    print(ans)


def __starting_point():
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)


__starting_point()
