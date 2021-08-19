import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def solve(N, K, X):
    A = [abs(x - X[0]) for x in X]
    ans = INF
    for i in range(N - K + 1):
        if ans > abs(X[i]) + A[i + K - 1] - A[i]:
            ans = abs(X[i]) + A[i + K - 1] - A[i]
    return ans


def main():
    (N, K, *X) = list(map(int, read().split()))
    ans = solve(N, K, X)
    ans = min(ans, solve(N, K, X[::-1]))
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
