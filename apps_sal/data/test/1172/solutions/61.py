MOD = 10 ** 9 + 7
S = input()
N = len(S)
(Acum, Ccum, Qcum) = ([0] * (N + 1), [0] * (N + 1), [0] * (N + 1))
for i in range(N):
    Acum[i + 1] = Acum[i] + 1 if S[i] == 'A' else Acum[i]
    Ccum[i + 1] = Ccum[i] + 1 if S[i] == 'C' else Ccum[i]
    Qcum[i + 1] = Qcum[i] + 1 if S[i] == '?' else Qcum[i]
ans = 0
for i in range(N):
    if S[i] != 'B' and S[i] != '?':
        continue
    (a, c, l, r) = (Acum[i], Ccum[N] - Ccum[i + 1], Qcum[i], Qcum[N] - Qcum[i + 1])
    res = pow(3, l + r - 2, MOD) * (3 * a + l) % MOD * (3 * c + r) % MOD
    ans = (ans + res) % MOD
print(ans)
