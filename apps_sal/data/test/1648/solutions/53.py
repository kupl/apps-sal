n, k = list(map(int, input().split()))
mod = 10**9 + 7


def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    return [w[0], w[1]]


mod = 10**9 + 7


def mod_inv(a, mod):
    x = extgcd(a, mod)[0]
    return (mod + x % mod) % mod


N = n - k + 1
combi = [0 for i in range(n + 1)]
combi[0] = 1
for i in range(1, N + 1):
    combi[i] = (combi[i - 1] * (N - i + 1) * mod_inv(i, mod)) % mod
fact = [0 for i in range(n + 1)]
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = (i * fact[i - 1]) % mod
for i in range(1, k + 1):
    print(((combi[i] * fact[k - 1] * pow(fact[k - i], -1, mod) * pow(fact[i - 1], -1, mod)) % mod))
