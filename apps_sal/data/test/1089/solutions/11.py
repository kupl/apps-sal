n, m, k = list(map(int, input().split()))


mod = 10 ** 9 + 7
N = 10 ** 6

inv_t = [0] + [1]
for i in range(2, N):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
    kai.append(kai[-1] * i % mod)
    rev_kai.append(rev_kai[-1] * inv_t[i] % mod)


def cmb(n, r):
    res = 1
    for i in range(r):
        res *= n * inv_t[r]
        res %= mod
        n -= 1
        r -= 1
    return res


def calc(n):
    res = 0
    for i in range(1, n):
        res += (n - i) * i
        res %= mod
    return res


ans = 0
ans += m * m * cmb(n * m - 2, k - 2) * calc(n)
ans %= mod

ans += n * n * cmb(n * m - 2, k - 2) * calc(m)
ans %= mod

print(ans)
