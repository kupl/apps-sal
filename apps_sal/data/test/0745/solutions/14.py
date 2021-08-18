fact = [1]
mod = 998244353
for i in range(1, 200001):
    fact.append((fact[-1] * i) % mod)

n, k = map(int, input().split())
same = k


def choose(n, r):
    return (fact[n] * pow(fact[r], mod - 2, mod) * pow(fact[n - r], mod - 2, mod)) % mod


def sterling(n, m):
    result = 0

    for i in range(n):

        if i % 2 == 0:
            result = (result + (choose(n, i) * pow(n - i, m, mod))) % mod
        else:
            result = (result - (choose(n, i) * pow(n - i, m, mod))) % mod

    return (result) % mod


if k > n - 1:
    print(0)
else:
    if k == 0:
        print(fact[n])
    else:
        print((2 * choose(n, n - k) * sterling(n - k, n)) % mod)
