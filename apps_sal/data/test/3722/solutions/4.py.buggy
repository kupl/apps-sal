U = 1010
mod = 10**9 + 7

fact = [1] * (U + 1)
fact_inv = [1] * (U + 1)

for i in range(1, U + 1):
    fact[i] = (fact[i - 1] * i) % mod
fact_inv[U] = pow(fact[U], mod - 2, mod)

for i in range(U, 0, -1):
    fact_inv[i - 1] = (fact_inv[i] * i) % mod


def perm(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[n - k]
    z %= mod
    return z


def comb(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[k]
    z *= fact_inv[n - k]
    z %= mod
    return z


# Qはソート済み（低次のものから並ぶようにする）
def poly_mul(P, Q):
    n = len(P)
    d, c = Q[0]
    if d:
        c = 0
    else:
        Q = Q[1:]
    for i in range(n - 1, -1, -1):
        P[i] *= c
        P[i] %= mod
        for j, b in Q:
            if j > i:
                break
            P[i] += P[i - j] * b
            P[i] %= mod

# Q[0] != 0 が必要


def poly_div(P, Q):
    n = len(P)
    d, c = Q[0]
    Q = Q[1:]
    inv = pow(c, mod - 2, mod)
    for i in range(n):
        for j, b in Q:
            if j > i:
                break
            P[i] -= P[i - j] * b
            P[i] %= mod
        P[i] *= inv
        P[i] %= mod


n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()
if aa == "A" and ab == "A":
    print(1)
    return
if bb == "B" and ab == "B":
    print(1)
    return
ans = 0
if (ab == "A" and ba == "A") or (ab == "B" and ba == "B"):
    for i in range(n):
        for j in range(n):
            if i + j != n - 1:
                continue
            ans += comb(i - 1, j)
            ans %= mod
else:
    F = [0] * 1010
    F[1] = 1
    F[2] = -1
    poly_div(F, ((0, 1), (1, -2)))
    ans = F[n - 1]
ans %= mod
print(ans)
