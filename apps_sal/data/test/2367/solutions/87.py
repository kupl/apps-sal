MOD = 10 ** 9 + 7


def prepare(n):
    nonlocal MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs


def pathVar(sx, sy, gx, gy):
    x = gx - sx
    y = gy - sy
    rst = modFacts[x + y]
    rst *= invs[x] * invs[y]
    rst %= MOD
    return rst


H, W, A, B = list(map(int, input().split()))
# H -= 1; W -= 1
modFacts, invs = prepare(H + W)

cnt = 0
while A > 0 and B > 0:
    x = H - A
    y = B - 1
    path1 = pathVar(0, 0, x, y)
    path2 = pathVar(x, y, H - 1, W - 1)
    cnt += path1 * path2
    cnt %= MOD
    A -= 1; B -= 1

ans = pathVar(0, 0, H - 1, W - 1)
print(((ans - cnt) % MOD))

