n = int(input())
C = [0 if input() == "A" else 1 for _ in range(4)]
mod = 10**9 + 7

l = 10**5
fac = [1] * l
facr = [1] * l

for i in range(l - 1):
    fac[i + 1] = fac[i] * (i + 1) % mod
facr[l - 1] = pow(fac[l - 1], mod - 2, mod)
for i in range(1, l)[::-1]:
    facr[i - 1] = facr[i] * i % mod


def combi(N: int, K: int) -> int:
    if N < K:
        return 0
    return fac[N] * facr[N - K] % mod * facr[K] % mod


if n == 3 or n == 2:
    print((1))
    return


if C[1] == 1 and C[3] == 1:
    # xBxB
    print((1))
    return
if C[1] == 0 and C[0] == 0:
    # AAxx
    print((1))
    return
if C[1] == C[2] == 1 and C[3] == 0:
    # xBBA
    ans = 0
    for i in range(1, n // 2 + 1):
        ans += combi(n - i - 1, i - 1)
        ans %= mod
    print(ans)
    return
if C[0] == 1 and C[1] == C[2] == 0:
    # BAAx
    ans = 0
    for i in range(1, n // 2 + 1):
        ans += combi(n - i - 1, i - 1)
        ans %= mod
    print(ans)
    return

if C[0] == C[2] == 1 and C[1] == 0:
    print((pow(2, n - 3, mod)))
    return
if C[1] == 1 and C[2] == C[3] == 0:
    print((pow(2, n - 3, mod)))
    return
