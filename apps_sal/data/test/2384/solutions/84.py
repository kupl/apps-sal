def main():
    from functools import lru_cache
    import sys
    sys.setrecursionlimit(10 ** 7)
    inf = 2 * 10 ** 14 + 1
    N = int(input())
    (*a,) = list(map(int, input().split()))

    @lru_cache(maxsize=None)
    def recursion(cur, need):
        """
        cur: pickableなindex
        """
        if cur >= N:
            if need == 0:
                return 0
            else:
                return -inf
        rest = N - cur
        if (rest + 1) // 2 < need:
            return -inf
        return max(a[cur] + recursion(cur + 2, need - 1), recursion(cur + 1, need))
    ans = recursion(0, N // 2)
    print(ans)


def __starting_point():
    main()


__starting_point()
