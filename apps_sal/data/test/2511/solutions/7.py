
N, K = map(int, input().split())
MOD = 10**9 + 7
es = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    es[a - 1].append(b - 1)
    es[b - 1].append(a - 1)


MAXN = K + 5
fac = [1, 1] + [0] * MAXN
finv = [1, 1] + [0] * MAXN
inv = [0, 1] + [0] * MAXN
for i in range(2, MAXN + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def nPr(n, r):
    if n < r:
        return 0
    return fac[n] * finv[n - r]


"""
curr とその親prevの色が決まっているときに、currの子nxtの色の塗り方の場合の数は
nPr(K-2, len(es[curr]) - 1)
Kのうちprevとcurrで２色使っていて、currにつながっているもののうち一つはprevだから、１引いたものが子供の数。
で、一番初めのノードoriginについて考えると、親はないのでノードorigin自体はK個の塗り方があり、その子には、nPr(K-1, len(es[origin]))の塗り方がある
あとはDFS的に子供の塗り方を決めていく

"""

checked = [False] * N
ans = K * nPr(K - 1, len(es[0]))
checked[0] = True

stack = []
for nxt in es[0]:
    stack.append(nxt)

while stack:
    curr = stack.pop()
    checked[curr] = True
    ans *= nPr(K - 2, len(es[curr]) - 1)
    if ans >= MOD: ans %= MOD
    for nxt in es[curr]:
        if not checked[nxt]:
            stack.append(nxt)

print(ans % MOD)
