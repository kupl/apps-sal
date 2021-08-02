def read_data():
    n, m = map(int, list(input().strip().split()))
    a = list(map(int, list(input().strip().split())))
    return n, m, a


def get_modinv(m):
    modinv = [-1 for _ in range(m + 1)]
    modinv[1] = 1
    for i in range(2, m + 1):
        modinv[i] = (-(div // i) * modinv[div % i]) % div
    return modinv


def partitions(n, k):
    if k > n:
        return 0
    val = 0
    sign = 1
    if k % 2 == 1:
        sign = -1
    for i in range(k + 1):
        v = (fact[k] * factinv[i] * factinv[k - i] * pow(i, n, div)) % div
        val += v * sign
        val %= div
        sign *= -1
    val *= factinv[k]
    return val % div


def solve():
    modinv = get_modinv(n + 1)
    for i in range(1, n + 2):
        fact.append(fact[-1] * i % div)
        factinv.append(factinv[-1] * modinv[i] % div)
    return ((partitions(n, k) + (n - 1) * partitions(n - 1, k)) * sum(a)) % div


div = 10**9 + 7
n, k, a = read_data()
fact, factinv = [1], [1]
print(solve())
