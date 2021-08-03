import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = list(map(int, readline().split()))

    R = [0] * K
    for n in range(1, N + 1):
        R[n % K] += 1

    ans = 0
    for a in range(K):
        b = (K - a) % K
        if 2 * b % K == 0:
            ans += R[a] * R[b] * R[b]

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
