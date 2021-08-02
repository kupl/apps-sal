import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)

    for i in range(N - 2):
        if S[i] == S[i + 1] or S[i] == S[i + 2]:
            print((i + 1, i + 3))
            return

    if S[N - 2] == S[N - 1]:
        print((N - 1, N))
        return

    print((-1, -1))
    return


def __starting_point():
    main()


__starting_point()
