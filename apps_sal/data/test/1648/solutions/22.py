def main():
    (N, K) = [int(a) for a in input().split(' ')]
    if N == K:
        for i in range(K):
            if i == 0:
                print(1)
            else:
                print(0)
        return 0
    lim = max([K, N - K]) + K + 1
    p = 1000000007
    f = []
    for i in range(lim):
        if i == 0:
            f.append(1)
        else:
            f.append(f[-1] * i % p)
    lf = len(f)
    fi = [0] * lf
    fi[-1] = inv(f[-1], p)
    for i in range(lf - 1):
        fi[lf - 1 - i - 1] = fi[lf - 1 - i] * (lf - 1 - i) % p

    def comb_p(n, k):
        if k < 0 or n < k:
            return 0
        return f[n] * (fi[k] * fi[n - k] % p) % p
    for i in range(1, K + 1):
        s = comb_p(K - 1, i - 1) * (comb_p(N - K - 1, i - 2) + 2 * comb_p(N - K - 1, i - 1) + comb_p(N - K - 1, i)) % p % p
        print(s)


def inv(a, p):
    power_a = [a]
    b_p = format(p - 2, 'b')
    ans = 1
    for i in range(len(b_p)):
        power_a.append(power_a[-1] ** 2 % p)
    for i in range(len(b_p)):
        if b_p[-i - 1] == '1':
            ans = ans * power_a[i] % p
    return ans


main()
