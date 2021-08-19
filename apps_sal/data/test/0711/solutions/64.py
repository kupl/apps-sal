from collections import defaultdict
(n, m) = map(int, input().split())
prime_list = defaultdict(int)
p = 2
while p <= 10 ** 4.5 + 5:
    if m % p == 0:
        prime_list[p] += 1
        m //= p
    else:
        p += 1
if m > 1:
    prime_list[m] += 1
MOD = 10 ** 9 + 7


def comb(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) % MOD * pow(i + 1, MOD - 2, MOD) % MOD
    return res


ans = 1
for k in prime_list.keys():
    ans *= comb(prime_list[k] + n - 1, prime_list[k])
    ans %= MOD
print(ans)
