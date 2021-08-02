import sys

K = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip('\n')

# ## COMBINATION (MOD) ###
N_MAX = 10**6  # 問題サイズに合わせて変えておく
MOD = 10**9 + 7

inv = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N_MAX + 2):
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)

# K 文字追加
ans = 0

ln = len(S)

p1 = 1
p2 = 1
s2 = pow(26, K, MOD)

for i in range(1, K + 2):

    ans += (p1 * p2 * s2) % MOD
    ans %= MOD

    # print(p1, p2, s2)

    # pre
    p1 = (p1 * (ln + i - 1) * inv[i]) % MOD
    p2 = (p2 * 25) % MOD

    # suf
    s2 = (s2 * inv[26]) % MOD

print(ans)
