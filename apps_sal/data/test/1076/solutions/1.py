nn = 2002002
P = 998244353
fa = [1] * (nn + 1)
fainv = [1] * (nn + 1)
for i in range(nn):
    fa[i + 1] = fa[i] * (i + 1) % P
fainv[-1] = pow(fa[-1], P - 2, P)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i + 1] * (i + 1) % P

N, M = list(map(int, input().split()))
invM1 = pow(M + 1, P - 2, P)
pre = 1
for i in range(2, N + 2):
    nu = ((M + i - 1) + (i - 1) * pre) * (M + 1) + M * (N - i + 1)
    de = invM1 * fainv[i - 1] % P * fa[i - 2] % P
    pre = nu * de % P
print(pre)
