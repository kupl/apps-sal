MOD = 10 ** 9 + 7
N = int(input())
C = list(sorted(map(int, input().split()), reverse=True))

ans = 0
pow_list = [1] * (N + 1)
for i in range(1, N + 1):
    pow_list[i] = (2 * pow_list[i - 1]) % MOD
base = pow_list[N]

# 基本戦略:コストが一番高いものを一番最後に変更する
for i, c in enumerate(C):
    now = pow_list[N - i - 1]
    tot = 0
    # コストがi番目に大きい値は、最後からi番目に変更を行うので
    # 左からi-bitまでに何個1が立ったかで加算回数が決まる
    if i >= 1:
        tot = pow_list[i] + i * pow_list[i - 1]
    else:
        tot = pow_list[i]
    ans += (tot * now * c) % MOD
    ans %= MOD
print(ans * base % MOD)
