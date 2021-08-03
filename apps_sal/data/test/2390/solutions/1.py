import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def calc_max(A):
    Amax = [0] * len(A)
    cal = 0
    for i, (x, v) in enumerate(A):
        cal += v
        if i == 0:
            Amax[i] = max(cal - x, 0)
        else:
            Amax[i] = max(cal - x, Amax[i - 1])

    return Amax


def solve(A, Amax, B, Bmax, ans):
    N = len(A)
    for i in range(N - 1):
        if ans < Amax[i] - A[i][0] + Bmax[N - i - 2]:
            ans = Amax[i] - A[i][0] + Bmax[N - i - 2]

    return ans


def main():
    N, C, *XV = list(map(int, read().split()))

    A = [0] * N
    for i, (x, v) in enumerate(zip(*[iter(XV)] * 2)):
        A[i] = (x, v)
    Amax = calc_max(A)

    B = [(C - x, v) for x, v in reversed(A)]
    Bmax = calc_max(B)

    ans = max(Amax[-1], Bmax[-1])
    ans = max(ans, solve(A, Amax, B, Bmax, ans))
    ans = max(ans, solve(B, Bmax, A, Amax, ans))

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
