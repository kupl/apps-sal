import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    P = [0] * (2 * N)
    for i in range(N):
        a, b = list(map(int, readline().split()))
        P[i] = (a, b, 0)
    for i in range(N, 2 * N):
        c, d = list(map(int, readline().split()))
        P[i] = (c, d, 1)

    P.sort(reverse=True)

    vec = [0] * (2 * N + 1)
    ans = 0

    for x, y, p in P:
        if p == 0:
            for i in range(y + 1, 2 * N + 1):
                if vec[i] > 0:
                    vec[i] -= 1
                    ans += 1
                    break
        else:
            vec[y] += 1

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
