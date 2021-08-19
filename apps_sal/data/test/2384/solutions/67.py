import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
inf = float('inf')


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    K = N // 2
    DP0 = [-inf] * N
    DP1 = [-inf] * N
    DP2 = [-inf] * N
    DP2[0] = A[0]
    DP2[1] = max(A[0], A[1])
    DP1[:2] = [0] * 2
    DP0[:4] = [0] * 4
    for i in range(2, N):
        if i % 2 == 0:
            DP2[i] = DP2[i - 2] + A[i]
            DP1[i] = max(DP2[i - 1], DP1[i - 2] + A[i])
            DP0[i] = max(DP1[i - 1], DP0[i - 2] + A[i])
        else:
            DP2[i] = max(DP2[i - 2] + A[i], DP2[i - 1])
            DP1[i] = max(DP1[i - 1], DP1[i - 2] + A[i])
            DP0[i] = max(DP0[i - 1], DP0[i - 2] + A[i])
    if N % 2 == 0:
        ans = DP2[N - 1]
    else:
        ans = DP1[N - 1]
    print(ans)


def __starting_point():
    main()


__starting_point()
