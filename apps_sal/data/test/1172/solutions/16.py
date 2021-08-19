s = input()
n = len(s)
mod = 10 ** 9 + 7
qcnt = [[0, 0] for i in range(n)]
Acnt = [0] * n
Ccnt = [0] * n
q = 0
for i in range(n - 1):
    if s[i] == '?':
        q += 1
        qcnt[i + 1][0] += 1
    elif s[i] == 'A':
        Acnt[i + 1] += 1
    qcnt[i + 1][0] += qcnt[i][0]
    Acnt[i + 1] += Acnt[i]
    qcnt[i + 1][0] %= mod
    Acnt[i + 1] %= mod
if s[-1] == '?':
    q += 1
for i in range(n - 1, 0, -1):
    if s[i] == '?':
        qcnt[i - 1][1] += 1
    elif s[i] == 'C':
        Ccnt[i - 1] += 1
    qcnt[i - 1][1] += qcnt[i][1]
    Ccnt[i - 1] += Ccnt[i]
    qcnt[i - 1][1] %= mod
    Ccnt[i - 1] %= mod
ans = 0
for i in range(n):
    if s[i] == 'B' or s[i] == '?':
        if qcnt[i][0] + qcnt[i][1] - 2 < 0:
            val = -(qcnt[i][0] + qcnt[i][1] - 2)
            p = pow(3, val, mod)
            q = pow(p, mod - 2, mod)
            ans += q % mod * (3 * Acnt[i] + qcnt[i][0]) * (3 * Ccnt[i] + qcnt[i][1]) % mod
        else:
            ans += pow(3, qcnt[i][0] + qcnt[i][1] - 2, mod) % mod * (3 * Acnt[i] + qcnt[i][0]) * (3 * Ccnt[i] + qcnt[i][1]) % mod
        ans %= mod
print(ans % mod)
