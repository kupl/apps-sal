from functools import lru_cache


def main():
    N = int(input())
    A = list(map(int, input().split()))
    x = 0
    for a in A[2:]:
        x ^= a
    (a, b) = (A[0], A[1])
    if (a ^ b ^ x) & 1 != 0:
        return -1

    @lru_cache(None)
    def helper(a, b, x):
        if a == 0:
            return 0 if a ^ b == x else None
        if (a ^ b) & 1 != x & 1:
            return None
        t1 = helper(a // 2, b // 2, x // 2)
        t2 = helper((a - 1) // 2, (b + 1) // 2, x // 2)
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2 * 2 + 1
        if t2 is None:
            return t1 * 2
        t1 = t1 * 2
        t2 = t2 * 2 + 1
        return min(t1, t2)
    r = helper(a, b, x)
    if r is None or r >= a:
        return -1
    return r


print(main())
