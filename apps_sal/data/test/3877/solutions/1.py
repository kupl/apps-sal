from functools import lru_cache
3


@lru_cache(maxsize=None)
def length(n):
    if n <= 1:
        return 1
    return 2 * length(n // 2) + 1


@lru_cache(maxsize=None)
def solve(n, l, r):
    if l > r:
        return 0
    if n <= 1:
        assert l == r and l == 1
        return n
    mid = length(n // 2) + 1
    if r < mid:
        return solve(n // 2, l, r)
    elif l > mid:
        return solve(n // 2, l - mid, r - mid)
    else:
        return n % 2 + solve(n // 2, l, mid - 1) + solve(n // 2, 1, r - mid)


(n, l, r) = list(map(int, input().split()))
print(solve(n, l, r))
