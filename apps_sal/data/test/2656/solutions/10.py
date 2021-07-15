K = int(input())
N = len(input()) + K
P = 10**9+7

nn = 2002002
fa = [1] * (nn+1)
fainv = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1) % P
fainv[-1] = pow(fa[-1], P-2, P)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i+1] * (i+1) % P

C = lambda a, b: fa[a] * fainv[b] % P * fainv[a-b] % P if 0 <= b <= a else 0

s = 0
po = 1
for i in range(K + 1):
    s = (s + C(N, i) * po) % P
    po = po * 25 % P
print(s)
