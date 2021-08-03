"""

AtCoder Beginner Contest 127  E - Cell Distance


x,yは独立して考えられるので分ける。
差分の絶対値の和の問題は
ある項について、＋として働くのが何回か、－として働くのが何回か
を考えてその分を足してあげればいい

例1の 2 x 2で考えると、x=2,y=1のについて、
xが＋に働くのは、x=2より小さい、(x,y)=(1,1),(1,2)
xが±0なのは、xが同じ、(x,y)=(2,2)
xが－に働くのはなし（x=2までなので）
的な。



Kについて考えると、ある駒a,b間のコストが求められる回数は、nCr(N*M-2, K-2)
（全部でK個選ぶときにa,bを先に選んで、残りのN-2からK-2個選ぶから。）

N x Mのマスで、(ax,ay)の物のコストについて、
X：+ax*(ax - 1) * N - ax * (M - ax) * N = ax*N*(ax-1-M+ax) = ax*N*(2ax-1-M)
これがマスの高さの分だけある(ayが1~Nまで)&これがnCr(N*M-2, K-2)回
Yも同様
"""


N, M, K = list(map(int, input().split()))

MOD = 10**9 + 7

MAXN = N * M + 10
fac = [1, 1] + [0] * MAXN
finv = [1, 1] + [0] * MAXN
inv = [0, 1] + [0] * MAXN
for i in range(2, MAXN + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def nCr(n, r):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


# X：+ax*(ax - 1) * N - ax * (M - ax) * N = ax*N*(ax-1-M+ax) = ax*N*(2ax-1-M)がN個＆nCr(N*M-2, K-2))回
ans = 0

for i in range(1, M + 1):
    tmp = (((((i * N) % MOD) * (2 * i - 1 - M)) % MOD) * N) % MOD

    #print("~~~", i*N, 2*i - 1 - M,tmp, nCr(N*M-2, K-2))

    tmp *= nCr(N * M - 2, K - 2)

    tmp %= MOD
    #print("pppp", tmp)
    ans += tmp

    ans %= MOD


for i in range(1, N + 1):
    tmp = (((((i * M) % MOD) * (2 * i - 1 - N)) % MOD) * M) % MOD

    tmp *= nCr(N * M - 2, K - 2)

    tmp %= MOD
    ans += tmp
    ans %= MOD


print(ans)
