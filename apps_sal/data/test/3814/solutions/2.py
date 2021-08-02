import numpy as np


def prepare(n, m):
    f = 1
    facts = [1]
    for i in range(1, n + 1):
        f = f * i % m
        facts.append(f)

    f = pow(f, m - 2, m)
    invs = [1] * (n + 1)
    invs[n] = f
    for i in range(n, 0, -1):
        f = f * i % m
        invs[i - 1] = f

    return facts, invs


def nik(n2, k, m):
    ret = 1
    yield ret
    for _ in range(k):
        ret = ret * n2 % m
        yield ret


n, m = list(map(int, input().split()))

facts, invs = prepare(n, m)
fn = facts[n]

np_range = np.arange(2, n + 4, dtype=np.int64)
dp = np.zeros(n + 2, dtype=np.int64)
dp[0] = 1

nn2 = [2]
for i in range(n):
    nn2.append(nn2[-1] ** 2 % m)

ans = 0
parity = 1

for i in range(n + 1):
    n2 = pow(2, n - i, m)
    coef = np.fromiter(nik(n2, i, m), dtype=np.int64)
    ncr = fn * invs[i] * invs[n - i] % m
    left = (dp[:i + 1] * coef % m).sum() % m
    right = nn2[n - i]
    ans = (ans + ncr * left % m * right % m * parity) % m
    dp[1:i + 2] = (dp[1:i + 2] * np_range[:i + 1] + dp[:i + 1]) % m
    parity *= -1

print(ans)
