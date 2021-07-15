def d_xor_sum(N):
    from functools import lru_cache

    @lru_cache()
    def f(k):
        # a+b<=k,a xor b <= k を満たす正整数(a,b)の組の個数(ただしa>=b)
        # N=0のとき(u,v)の組は(0,0)の1通り
        # N=1のとき(0,0),(1,1)の2通り
        return (1, 2)[k] if k <= 1 else f(k // 2) + f((k - 1) // 2) + f((k - 2) // 2)

    ans = f(N) % (10**9 + 7)
    return ans

N = int(input())
print(d_xor_sum(N))
