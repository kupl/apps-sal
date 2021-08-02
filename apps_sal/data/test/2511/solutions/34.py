import sys
sys.setrecursionlimit(100000)

N, K = map(int, input().split())
SIZE = 10**5 + 1; MOD = 10**9 + 7  # 998244353 #ここを変更する

SIZE += 1
inv = [0] * SIZE  # inv[j] = j^{-1} mod MOD
fac = [0] * SIZE  # fac[j] = j! mod MOD
finv = [0] * SIZE  # finv[j] = (j!)^{-1} mod MOD
inv[1] = 1
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
for i in range(2, SIZE):
    inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
    fac[i] = fac[i - 1] * i % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def narabekae(n, r):  # nPr mod MOD の計算
    if n - r < 0:
        return 0
    return fac[n] * finv[n - r] % MOD


branch = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    branch[a - 1].append(b - 1)
    branch[b - 1].append(a - 1)

ans = 1


def draw(parent, nord):
    nonlocal ans
    children = len(branch[nord]) - (parent != -1)
    if children == 0:
        return
    # (K-2)*(K-1)*... をchildrenの数だけ掛ける。
    ans = ans * narabekae(K - 1 - (parent != -1), children) % MOD
    for b in branch[nord]:
        if b != parent:
            draw(nord, b)


draw(-1, 0)
print(ans * K % MOD)
