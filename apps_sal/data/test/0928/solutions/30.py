import sys


def solve(N: int, K: int, a: 'List[int]'):
    (su, left, ans) = (0, 0, 0)
    for right in range(N):
        su += a[right]
        while su - a[left] >= K:
            su -= a[left]
            left += 1
        ans += left + (su >= K)
        right += 1
    return ans


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    a = [int(next(tokens)) for _ in range(N)]
    print(solve(N, K, a))


def __starting_point():
    main()


__starting_point()
