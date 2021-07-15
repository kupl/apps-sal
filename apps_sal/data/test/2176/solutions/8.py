from operator import itemgetter
import sys


class Combination:
    '''MOD上の
    計算量：階乗・逆元テーブルの作成O(N)
    nCkを求めるO(1)'''

    def __init__(self, n, MOD):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % MOD)


input = sys.stdin.readline
n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
MOD = 998244353
comb = Combination(n, MOD)
memo1 = {}
memo2 = {}

for i in range(n):
    tmp1, tmp2 = p[i]
    if tmp1 not in memo1:
        memo1[tmp1] = 1
    else:
        memo1[tmp1] += 1
    if tmp2 not in memo2:
        memo2[tmp2] = 1
    else:
        memo2[tmp2] += 1

ans = 0

tmp = 1
for i in memo1:
    tmp *= comb.fact[memo1[i]]
    tmp %= MOD
ans += tmp
ans %= MOD

tmp = 1
for i in memo2:
    tmp *= comb.fact[memo2[i]]
    tmp %= MOD
ans += tmp
ans %= MOD

p = sorted(p, key = itemgetter(1))
p = sorted(p, key = itemgetter(0))
for i in range(n-1):
    if p[i][1] > p[i+1][1]:
        ans = comb.fact[n] - ans
        ans %= MOD
        print(ans)
        return
cnt = 1
tmp = 1
for i in range(n-1):
    if p[i][0] == p[i+1][0] and p[i][1] == p[i+1][1]:
        cnt += 1
    else:
        tmp *= comb.fact[cnt]
        tmp %= MOD
        cnt = 1
tmp *= comb.fact[cnt]
tmp %= MOD
ans -= tmp

ans = comb.fact[n] - ans
ans %= MOD
print(ans)
