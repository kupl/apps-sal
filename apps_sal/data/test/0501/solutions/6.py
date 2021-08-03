MOD = 1000000007


def evensum(n):
    n //= 2
    return (n * (n + 1)) % MOD


def oddsum(n):
    a = (n * (n + 1)) // 2
    a %= MOD
    a -= evensum(n - 1)
    a %= MOD
    return a


def cs(n):
    i = 0
    cn = 1
    tot = 0
    so = -1
    se = 0
    while tot < n:
        cur = min(cn, n - tot)
        if i % 2 == 0:
            so += 2 * cur
        else:
            se += 2 * cur
        cn *= 2
        tot += cur
        i += 1
    ans = 0
    if se > 0:
        ans += evensum(se)
    if so > -1:
        ans += oddsum(so)
    ans %= MOD
    return ans


L, R = list(map(int, input().split()))
ans = cs(R)
if L > 1:
    ans -= cs(L - 1)
ans %= MOD
print(ans)
