
def main():
    from collections import defaultdict

    INF = 40 * 100 + 1

    N, Ma, Mb = list(map(int, input().split()))

    memo = defaultdict(lambda: INF)

    for _ in range(N):
        ai, bi, ci = list(map(int, input().split()))
        x = Ma * bi - Mb * ai

        for key, value in tuple(memo.items()):
            memo[key + x] = min(
                memo[key + x],
                value + ci
            )
        memo[x] = min(memo[x], ci)

    print((memo[0] if 0 in memo else -1))


def __starting_point():
    main()


__starting_point()
