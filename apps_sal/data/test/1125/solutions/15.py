import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    xorR = 0
    for i in range(2, N):
        xorR ^= A[i]
    rbit = [0] * 41
    K = xorR
    for i in range(41):
        rbit[i] = K % 2
        K //= 2

    D = A[0] + A[1] - xorR
    if D < 0 or D % 2 == 1:
        print(-1)
        return 0
    else:
        D //= 2
        if D > A[0]:
            print(-1)
            return 0

        K = D
        dbit = [0] * 41
        for i in range(41):
            dbit[i] = K % 2
            K //= 2

        A0 = D
        for i in range(41):
            if rbit[40 - i] == dbit[40 - i] and rbit[40 - i] == 1:
                print(-1)
                return 0
            else:
                if rbit[40 - i] == 1:
                    if A0 + pow(2, 40 - i) <= A[0]:
                        A0 += pow(2, 40 - i)
        if A0 > 0:
            print(A[0] - A0)
        else:
            print(-1)

    return 0


def __starting_point():
    solve()


__starting_point()
