def d_xor_sum(N):
    from functools import lru_cache

    @lru_cache()
    def f(k):
        return (1, 2)[k] if k <= 1 else f(k // 2) + f((k - 1) // 2) + f((k - 2) // 2)

    ans = f(N) % (10**9 + 7)
    return ans


N = int(input())
print(d_xor_sum(N))
