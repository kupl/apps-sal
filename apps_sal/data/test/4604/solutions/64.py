import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    A.sort()

    ok = True
    if len(A) % 2 == 0:
        for i in range(N // 2):
            if not A[2 * i] == A[2 * i + 1] == 2 * i + 1:
                ok = False
                break
    else:
        if A[0] != 0:
            ok = False
        else:
            for i in range(N // 2):
                if not A[2 * i + 1] == A[2 * i + 2] == 2 * i + 2:
                    ok = False
                    break

    if ok:
        ans = pow(2, N // 2, MOD)
    else:
        ans = 0

    print(ans)

    return


def __starting_point():
    main()

__starting_point()
