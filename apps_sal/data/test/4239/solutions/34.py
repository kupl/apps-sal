def fn(n, a):
    res = 0
    while n > 0:
        res += n % a
        n //= a

    return res


def solve(N):

    ans = 10 ** 5
    for i in range(N + 1):
        tmp = fn(i, 6) + fn(N - i, 9)
        ans = min(ans, tmp)

    return ans


def __starting_point():
    N = int(input())
    print((solve(N)))


__starting_point()
