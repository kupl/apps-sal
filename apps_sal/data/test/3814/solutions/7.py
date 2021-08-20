import numpy as np


def prepare(n, m):
    f = 1
    for i in range(1, n + 1):
        f = f * i % m
    fn = f
    inv = [1] * (n + 1)
    f = pow(f, m - 2, m)
    inv[n] = f
    for i in range(n, 0, -1):
        f = f * i % m
        inv[i - 1] = f
    return (fn, inv)


def a_x(a, x, m):
    ret = 1
    yield ret
    for _ in range(x):
        ret = ret * a % m
        yield ret


(N, M) = list(map(int, input().split()))
(fn, inv) = prepare(N, M)
stir2 = np.zeros(N + 2, dtype=np.int64)
stir2[0] = 1
upd = np.arange(2, N + 3, dtype=np.int64)
ex2 = [2]
for i in range(N):
    ex2.append(ex2[-1] ** 2 % M)
ans = 0
si = 1
for i in range(N + 1):
    nCi = fn * inv[i] * inv[N - i] % M
    i_with = np.fromiter(a_x(pow(2, N - i, M), i, M), dtype=np.int64)
    i_on = (stir2[:i + 1] * i_with % M).sum() % M
    ans = (ans + nCi * i_on % M * ex2[N - i] % M * si) % M
    stir2[1:i + 2] = (stir2[1:i + 2] * upd[:i + 1] + stir2[:i + 1]) % M
    si *= -1
print(ans)
