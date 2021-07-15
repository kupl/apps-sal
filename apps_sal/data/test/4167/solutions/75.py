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
    for i in range(1, N + 1):
        R[i % K] += 1

    ans = 0
    for a in range(K):
        b = c = (K - a) % K
        if (b + c) % K == 0:
            ans += R[a] * R[b] * R[c]

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
