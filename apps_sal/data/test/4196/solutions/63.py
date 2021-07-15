import sys
from math import gcd

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 2:
        ans = max(A)
        print(ans)
        return

    L_GCD = [0] * N
    L_GCD[0] = A[0]
    for i in range(N - 1):
        L_GCD[i + 1] = gcd(L_GCD[i], A[i + 1])

    R_GCD = [0] * N
    R_GCD[-1] = A[-1]
    for i in reversed(list(range(N - 1))):
        R_GCD[i] = gcd(R_GCD[i + 1], A[i])

    ans = 1
    for i in range(N):
        if i == 0:
            ans = max(ans, R_GCD[1])
        elif i == N - 1:
            ans = max(ans, L_GCD[-2])
        else:
            res = gcd(L_GCD[i - 1], R_GCD[i + 1])
            ans = max(ans, res)

    print(ans)


def __starting_point():
    main()

__starting_point()
