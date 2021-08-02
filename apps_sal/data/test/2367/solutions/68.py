mod = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append(fact[-1] * i % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


def combi_mod(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


H, W, A, B = list(map(int, input().split()))

if B < W / 2:
    not_ans = 0
    total = combi_mod((H - 1) + (W - 1), H - 1, mod)
    for i in range(B):
        sq1h = H - A
        sq1w = i + 1
        sq2h = A
        sq2w = W - i
        n = combi_mod((sq1h - 1) + (sq1w - 1), (sq1h - 1), mod) * combi_mod((sq2h - 1) + (sq2w - 1), (sq2h - 1), mod) % mod
        not_ans = (not_ans + n) % mod
    ans = (total - not_ans) % mod
    print(ans)

else:
    ans = 0
    for i in range(B, W):
        sq1h = H - A
        sq1w = i + 1
        sq2h = A
        sq2w = W - i
        n = combi_mod((sq1h - 1) + (sq1w - 1), (sq1h - 1), mod) * combi_mod((sq2h - 1) + (sq2w - 1), (sq2h - 1), mod)
        ans = (ans + n) % mod
    ans %= mod
    print(ans)
