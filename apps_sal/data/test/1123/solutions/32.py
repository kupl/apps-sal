
mod = pow(10, 9) + 7

def main():
    N, K = list(map(int, input().split()))
    table = [0]*(K+1)
    for k in range(K, 0, -1):
        m = K//k
        tmp = pow(m, N, mod)
        for l in range(2, m+1):
            tmp -= table[l*k]
            tmp %= mod
        table[k] = tmp

    ans = 0
    for i in range(len(table)):
        ans += (i * table[i])%mod
    ans %= mod
    #print(table)
    print(ans)


def __starting_point():
    main()

__starting_point()
