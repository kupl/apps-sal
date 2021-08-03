from sys import stdin, stdout


MOD = 10 ** 9 + 7


def bin_pow(n, k):
    res = 1

    while k:
        if k & 1:
            res = (res * n) % MOD

        n = (n * n) % MOD
        k >>= 1

    return res


x, k = map(int, stdin.readline().split())

if x == 0:
    stdout.write('0')
else:
    ans = (bin_pow(2, k + 1) * x - bin_pow(2, k) + 1) % MOD
    stdout.write(str(ans))
