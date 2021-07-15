N,M,K =map(int, input().split())
mod = 10**9 + 7

# cmbが10**10くらいだけど求められるか？って感じ
# 問題読み違えていた。。。N*M <= 2*10**5だ。。。まあ普通だ。
# もうライブラリ使おう。昔nCrのrが小さい時の工夫とかあったけど今回は大丈夫だ。

# https://ikatakos.com/pot/programming_algorithm/number_theory/mod_combination
import numpy as np
 
def prepare(n, MOD):
    nrt = int(n ** 0.5) + 1
    nsq = nrt * nrt
    facts = np.arange(nsq, dtype=np.int64).reshape(nrt, nrt)
    facts[0, 0] = 1
    for i in range(1, nrt):
        facts[:, i] = facts[:, i] * facts[:, i - 1] % MOD
    for i in range(1, nrt):
        facts[i] = facts[i] * facts[i - 1, -1] % MOD
    facts = facts.ravel().tolist()
 
    invs = np.arange(1, nsq + 1, dtype=np.int64).reshape(nrt, nrt)
    invs[-1, -1] = pow(facts[-1], MOD - 2, MOD)
    for i in range(nrt - 2, -1, -1):
        invs[:, i] = invs[:, i] * invs[:, i + 1] % MOD
    for i in range(nrt - 2, -1, -1):
        invs[i] = invs[i] * invs[i + 1, 0] % MOD
    invs = invs.ravel().tolist()
 
    return facts, invs

facts, invs = prepare(N*M+10,mod)
def cmb(n,r,MOD):
  return (((facts[n] * invs[n-r]) % mod) * invs[r]) % mod

## シグマを分離すること。２点i,jの選び方数、かけることのi,jの距離とする。あとはこれに２点以外の選び方のパターン数をかければ良い
# X,Yを独立して考える
# 例えばXについて考えると、使う列の選び方がN*2, 使う行の選び方はM-dis(1ならM-1だし、M-1離れてるのは１個しか選べない）
# disは距離が答えに寄与するから
# cmb()はその２点以外の選び方の個数の話。
#  もちろん他のi,jについて見たら同じ盤面何度も見てるけど、今のi,jに関する値しか計算してないからOK
ans = 0

for dis in range(M):
  ans += N**2 * (M-dis) * dis * cmb(N*M-2, K-2, mod)
  ans %= mod
for dis in range(N):
  ans += M**2 * (N-dis) * dis * cmb(N*M-2, K-2, mod)
  ans %= mod

print(ans)
