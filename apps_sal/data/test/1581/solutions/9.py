def solve():
    N, K = map(int, input().split())

    U = []; V = []
    for x in range(1, int(N**.5) + 1):
        U.append(x)
        if x < N // x:
            V.append(N // x)
    V.reverse(); U.extend(V)

    L = len(U)
    prv = 0
    R = []
    for x in U:
        R.append(x - prv)
        prv = x

    def gen(it):
        MOD = 10**9 + 7
        r = 0
        for p, s in it:
            r = (p * s + r) % MOD
            yield r

    S = [1] * (L + 1)
    S[-1] = 0
    for k in range(K):
        S[L - 1::-1] = gen(zip(R, S))
    print(S[0])


solve()
