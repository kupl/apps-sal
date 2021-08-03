import sys

K = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip('\n')

# ## COMBINATION (MOD) ###
N_MAX = 10**6  # 問題サイズに合わせて変えておく
MOD = 10**9 + 7

inv = [0] * (N_MAX + 2)
inv[0] = 0  # 逆元テーブル計算用テーブル
inv[1] = 1

for i in range(2, N_MAX + 2):
    q, r = divmod(MOD, i)
    inv[i] = -inv[r] * q % MOD


# K 文字追加
ans = 0

ln = len(S)

p = pow(26, K, MOD)

for i in range(1, K + 2):

    ans += p % MOD
    ans %= MOD

    # pre
    p = p * (ln + i - 1) * inv[i] * 25 * inv[26] % MOD

    # suf
    # s2 = (s2 * inv[26]) % MOD

print(ans)
