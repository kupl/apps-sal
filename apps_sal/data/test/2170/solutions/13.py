#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    if sys.argv[-1] == 'ONLINE_JUDGE':
        import numba
        from numba.pycc import CC
        i8 = numba.int64
        cc = CC('my_module')
 
        def cc_export(f, signature):
            cc.export(f.__name__, signature)(f)
            return numba.njit(f)
 
            fact_table = cc_export(fact_table, (i8, i8))
            main = cc_export(main, (i8, i8, i8))
            cc.compile()

    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    n, m = list(map(int, input().split()))

    #output
    mod = pow(10, 9) + 7

    n_ = 5 * pow(10, 5) + 5
    fun = [1] * (n_+1)
    for i in range(1, n_+1):
        fun[i] = fun[i-1] * i % mod
    rev = [1] * (n_+1)
    rev[n_] = pow(fun[n_], mod-2, mod)
    for i in range(n_-1, 0, -1):
        rev[i] = rev[i+1] * (i+1) % mod
    def cmb(n,r):
        if n < 0 or r < 0 or r > n: return 0
        return fun[n] * rev[r] % mod * rev[n-r] % mod
    def perm(n, r):
        if n < 0 or r < 0 or r > n: return 0
        return fun[n] * rev[n-r] % mod

    #Aを1, 2, ..., nとする。
    #求める写像の総数をs(n, m)とする。
    #s(n, m) = sum(k=0, n)(cmb(n, k)* (-1)^k * cmb(m-k, n-k)*(n-k)!)

    import math
    answer = 0
    for i in range(n+1):
        temp = perm(n, i) * cmb(m, i) * pow(perm(m-i, n-i), 2)
        temp %= mod
        if i % 2 == 0:
            answer += temp
        else:
            answer -= temp
    print((answer % mod))

    #N = 1のときなどcorner caseを確認！
def __starting_point():
    main()

__starting_point()
