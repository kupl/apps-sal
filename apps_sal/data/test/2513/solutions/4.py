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

    ans = -1
    for last, first in ((0, 0), (0, 1), (1, 0), (1, 1)):
        vec = [0] * N
        vec[-1] = last
        vec[0] = first
        for i in range(N):
            if vec[i] == 0:
                if S[i] == 'o':
                    vec[(i + 1) % N] = vec[i - 1]
                else:
                    vec[(i + 1) % N] = 1 - vec[i - 1]
            else:
                if S[i] == 'o':
                    vec[(i + 1) % N] = 1 - vec[i - 1]
                else:
                    vec[(i + 1) % N] = vec[i - 1]

        if vec[-1] == last and vec[0] == first:
            ans = ''.join('S' if a == 0 else 'W' for a in vec)
            break

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
