nn = 200200
P = 998244353

fa = [1] * (nn + 1)
fainv = [1] * (nn + 1)
for i in range(nn):
    fa[i + 1] = fa[i] * (i + 1) % P
fainv[-1] = pow(fa[-1], P - 2, P)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i + 1] * (i + 1) % P


def C(a, b): return fa[a] * fainv[b] % P * fainv[a - b] % P if 0 <= b <= a else 0


N, K = list(map(int, input().split()))
if K == 0:
    print(fa[N])
    return
if K >= N:
    print(0)
    return

a = N - K
ans = 0
for i in range(a + 1):
    ans = (ans + pow(a - i, N, P) * C(a, i) * (-1 if i & 1 else 1)) % P

ans = ans * 2 * C(N, a) % P
print(ans)
