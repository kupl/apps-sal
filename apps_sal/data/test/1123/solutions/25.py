
N, K = list(map(int, input().split()))
mod = 10**9 + 7


def main():
    b = N
    blis = []
    c = 0
    while b > 0:
        if b & 1 == 1:
            blis.append(c)
        c += 1
        b >>= 1

    def modpow(a, blis=blis, c=c):
        if a == 1:
            return 1
        else:
            res = 1
            li = []
            for _ in range(c):
                li.append(a % mod)
                a = a * a % mod
            for item in blis:
                res = res * li[item] % mod
            return res

    fact_count = [0 for _ in range(K + 1)]
    for k in range(1, K + 1):
        fact_count[k] = K // k

    ans = 0
    count = [0 for _ in range(K + 1)]
    for k in range(K, 0, -1):
        x = 1 * fact_count[k]
        cc = modpow(x)
        j = 2 * k
        l = 2
        while(j <= K):
            cc -= count[j]
            l += 1
            j = k * l
        count[k] = cc
        cc = cc * k % mod
        ans += cc
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
