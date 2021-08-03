def memoize(f):
    memo = {}

    def helper(*x):
        x = tuple(x)
        if x not in memo:
            memo[x] = f(*x)
        return memo[x]
    return helper


n, d, *_ = list(map(int, input().split()))
*x, = list(map(int, input().split()))


x.sort()


@memoize
def solve(d, li, ri):
    if x[ri] - x[li] <= d:
        return 0
    else:
        return min(solve(d, li + 1, ri), solve(d, li, ri - 1)) + 1


print(solve(d, 0, len(x) - 1))
