import numpy as np
N, M, K = map(int, input().split())
mod = 10**9 + 7


def prepare(n, MOD):
    nrt = int(n ** 0.5) + 1
    nsq = nrt * nrt
    facts = np.arange(nsq, dtype=np.int64).reshape(nrt, nrt)
    facts[0, 0] = 1
    for i in range(1, nrt):
        facts[:, i] = facts[:, i] * facts[:, i - 1] % MOD
    for i in range(1, nrt):
        facts[i] = facts[i] * facts[i - 1, -1] % MOD
    facts = facts.ravel().tolist()

    invs = np.arange(1, nsq + 1, dtype=np.int64).reshape(nrt, nrt)
    invs[-1, -1] = pow(facts[-1], MOD - 2, MOD)
    for i in range(nrt - 2, -1, -1):
        invs[:, i] = invs[:, i] * invs[:, i + 1] % MOD
    for i in range(nrt - 2, -1, -1):
        invs[i] = invs[i] * invs[i + 1, 0] % MOD
    invs = invs.ravel().tolist()

    return facts, invs


facts, invs = prepare(N * M + 10, mod)


def cmb(n, r, MOD):
    return (((facts[n] * invs[n - r]) % mod) * invs[r]) % mod


ans = 0

for dis in range(M):
    ans += N**2 * (M - dis) * dis * cmb(N * M - 2, K - 2, mod)
    ans %= mod
for dis in range(N):
    ans += M**2 * (N - dis) * dis * cmb(N * M - 2, K - 2, mod)
    ans %= mod

print(ans)
