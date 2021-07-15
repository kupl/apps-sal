s = input()
MOD = 10 ** 9 + 7
num = 0
N = len(s)
R = [0] * (N + 1)
L = [0] * (N + 1)
d = []
for i in range(N):
    if s[i] == ')':
        R[i + 1] = 1
    else:
        L[i + 1] = 1
        d.append(i)

for i in range(1, N + 1):
    R[i] += R[i - 1]
    L[i] += L[i - 1]


M = 200005
fact = [0] * M
fact[0] = 1
for i in range(1, M):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD

rfact = [0] * M
rfact[M - 1] = pow(fact[M - 1], MOD - 2, MOD)
for i in range(M - 2, -1, -1):
    rfact[i] = rfact[i + 1] * (i + 1)
    rfact[i] %= MOD


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * rfact[n - k] * rfact[k] % MOD


for i in d:
    if s[i] == '(':
        l = L[i + 1] - 1
        r = R[N] - R[i + 1]
        num += comb(l + r, l + 1)
        num %= MOD

print(num)

