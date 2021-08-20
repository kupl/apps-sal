from functools import reduce


def solve(*args: str) -> str:
    (n, k) = list(map(int, args[0].split()))
    A = sorted(map(int, args[1].split()))
    mod = 10 ** 9 + 7
    if n == k:
        return str(reduce(lambda a, b: a * b % mod, A, 1))
    if k % 2 and A[-1] < 0:
        return str(reduce(lambda a, b: a * b % mod, A[n - k:], 1))
    (l, r) = (0, n - 1)
    count = 0
    ret = 1
    if k % 2:
        ret *= A[-1]
        r -= 1
        count += 1
    while count < k - 1:
        pos = max(0, A[r] * A[r - 1])
        neg = max(0, A[l] * A[l + 1])
        if pos <= neg:
            ret *= neg
            l += 2
        else:
            ret *= pos
            r -= 2
        ret %= mod
        count += 2
    return str(ret % mod)


def __starting_point():
    print(solve(*open(0).read().splitlines()))


__starting_point()
