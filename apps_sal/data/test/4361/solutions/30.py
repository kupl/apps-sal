def solve(N, K, h):
    h.sort()
    ans = 10 ** 9
    for i in range(K - 1, N):
        ans = min(ans, h[i] - h[i - (K - 1)])
    print(ans)


def __starting_point():
    N, K = list(map(int, input().split()))
    h = [int(input()) for _ in range(N)]
    solve(N, K, h)


__starting_point()
