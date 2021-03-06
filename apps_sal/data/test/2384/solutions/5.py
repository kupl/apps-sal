import sys
MOD = 1000000007


def solve(N: int, A: 'List[int]'):
    from collections import defaultdict
    M = N // 2

    def get_range(idx):
        r = (N - idx) // 2 + 1
        return list(range(max(0, M - r), idx // 2 + 1 + 1))
    dp_a = defaultdict(lambda: -float('inf'))
    dp_s = defaultdict(lambda: -float('inf'))
    dp_s[0, -1] = 0
    for i in range(N):
        for j in get_range(i):
            dp_s[j, i] = max(dp_s[j, i], dp_a[j, i - 1], dp_s[j, i - 1])
            dp_a[j, i] = max(dp_a[j, i], dp_s[j, i], dp_s[j - 1, i - 1] + A[i])
    print(max(max((v for ((j, i), v) in list(dp_a.items()) if j == M)), max((v for ((j, i), v) in list(dp_s.items()) if j == M))))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, A)


def __starting_point():
    main()


__starting_point()
