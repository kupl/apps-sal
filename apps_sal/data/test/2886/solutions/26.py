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

    a, b = -1, -1
    for i in range(N):
        if i < N - 1 and S[i] == S[i + 1]:
            a, b = i + 1, i + 2
            break
        elif i < N - 2 and S[i] == S[i + 2]:
            a, b = i + 1, i + 3
            break

    print((a, b))
    return


def __starting_point():
    main()


__starting_point()
