# inverse x^(-1)
def inv(x):
    nonlocal mod
    return pow(x, mod - 2, mod)


mod = 10**9 + 7
N = int(input())
C = [0]
C.extend(sorted(list(map(int, input().split())), reverse=True))  # 1-indexed, 降順

# print(C)
# C[i]が最後からj番目に操作される（コストが C[i]*j 掛かる）のは，c[1]~C[i-1]にj-1個操作すべきもの，すなわち，C[i]以上のものがあるとき。
# C[i+1]~C[N]の選び方は自由。
# ⇒ combi(i-1, j-1)*2**(N-i) を掛ける。
# 総和を計算すると，結局，2**N * Σ[i=1->N](2**(N-i)*Ci*(2**(i-2)*(i-1) + 2**(i-1))) になる

pow2 = [1]
for k in range(1, N + 1):
    pow2.append(pow2[-1] * 2 % mod)

# print(pow2)

ans = 0
for i in range(1, N + 1):
    temp = pow2[N - i] * C[i] * ((0 if i == 1 else (pow2[i - 2] * (i - 1))) + pow2[i - 1]) % mod
    ans = (ans + temp) % mod

ans = ans * pow2[N] % mod

print(ans)
