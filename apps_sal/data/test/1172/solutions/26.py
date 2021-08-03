S = input()
nQ_r = S.count('?')
nC_r = S.count('C')
nQ_l = 0
nA_l = 0
N = len(S)
mod = 10**9 + 7

pow3 = [1] * N
p = 1
for i in range(1, N):
    pow3[i] = p = p * 3 % mod

ans = 0
for n, c in enumerate(S):
    if c == 'C':
        nC_r -= 1
    if c == '?':
        nQ_r -= 1

    if n > 0 and n < N - 1 and (c == 'B' or c == '?'):
        p = (nQ_l * pow3[max(0, nQ_l - 1)] + nA_l * pow3[nQ_l]) % mod
        q = (nQ_r * pow3[max(0, nQ_r - 1)] + nC_r * pow3[nQ_r]) % mod
        ans += p * q
        ans %= mod

    if c == 'A':
        nA_l += 1
    if c == '?':
        nQ_l += 1

print(ans)
