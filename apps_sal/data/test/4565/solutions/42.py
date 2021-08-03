import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    east = [0] * (N + 1)
    west = [0] * (N + 1)
    for i in range(N):
        east[i + 1] = east[i] + (1 if S[i] == 'E' else 0)
        west[i + 1] = west[i] + (1 if S[i] == 'W' else 0)

    ans = INF
    for i in range(N):
        if ans > west[i] + east[N] - east[i + 1]:
            ans = west[i] + east[N] - east[i + 1]

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
