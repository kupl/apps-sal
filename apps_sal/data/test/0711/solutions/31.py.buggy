def factorize(n):
    '''
    素因数分解をする。
    タプルの配列にしようと思ったけど、逐次割り算する過程で次数を増やせないじゃん。
    二重配列?
    dictにしよう。
    '''
    if n == 1:
        raise('n >= 2')

    factor = {}
    div = 2
    while True:
        if div * div > n:
            factor[n] = factor.get(n, 0) + 1
            return factor

        if n % div == 0:
            n //= div
            factor[div] = factor.get(div, 0) + 1
        else:
            div += 1


n, m = list(map(int, input().split()))

if m == 1:
    print((1))
    return

factor = factorize(m)


max_len = n + 100  # 適宜変更する
mod = 10**9 + 7


def modinv(x):
    '''
    xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
    Python標準のpowは割った余りを出すことも可能。
    '''
    return pow(x, mod - 2, mod)


# 二項係数の左側の数字の最大値を max_len　とする。nとかだと他の変数と被りそうなので。
# factori_table = [1, 1, 2, 6, 24, 120, ...] 要は factori_table[n] = n!
# 計算時間はO(max_len * log(mod))
modinv_table = [-1] * (max_len + 1)
modinv_table[0] = None  # 万が一使っていたときにできるだけ早期に原因特定できるようにしたいので、Noneにしておく。
factori_table = [1] * (max_len + 1)
factori_inv_table = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    factori_table[i] = factori_table[i - 1] * (i) % mod

modinv_table[1] = 1
for i in range(2, max_len + 1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod
    factori_inv_table[i] = factori_inv_table[i - 1] * modinv_table[i] % mod


def binomial_coefficients(n, k):
    '''
    n! / (k! * (n-k)! )
    0 <= k <= nを満たさないときは変な値を返してしまうので、先にNoneを返すことにする。
    場合によっては0のほうが適切かもしれない。
    '''
    if not 0 <= k <= n:
        return None
    return (factori_table[n] * factori_inv_table[k] * factori_inv_table[n - k]) % mod


ans = 1
mod = 10**9 + 7
for prime, power in list(factor.items()):
    # ans *= n H power = n+power-1 C power
    ans *= binomial_coefficients(n + power - 1, power)
    ans %= mod

print(ans)
