import sys
sys.setrecursionlimit(10 ** 7)
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
dp1 = [1, 0]
dp2 = [1, K - 1]
for i in range(1 + N // 2):
    (d1, d2) = (dp1[-1], dp2[-1])
    dp1.append(d2)
    dp2.append(((K - 1) * d1 + (K - 2) * d2) % mod)
ans = 1
dif = (K - 2) * pow(K - 1, mod - 2, mod) % mod
AO = A[::2]
AE = A[1::2]
if all((a == -1 for a in AO)):
    ans = K * pow(K - 1, len(AO) - 1, mod) % mod
else:
    AO = [0] + AO + [0]
    mc = 0
    l = -2
    r = -2
    for (i, a) in enumerate(AO[1:], 1):
        if a == -1:
            if AO[i - 1] != -1:
                l = AO[i - 1]
            mc += 1
        else:
            r = a
            if AO[i - 1] == a:
                ans = 0
                break
            elif mc:
                if not l or not r:
                    ans = ans * pow(K - 1, mc, mod) % mod
                elif l == r:
                    ans = ans * dp2[mc] % mod
                else:
                    ans = ans * (dp2[mc] * dif + dp1[mc]) % mod
            mc = 0
if all((a == -1 for a in AE)):
    ans = ans * K * pow(K - 1, len(AE) - 1, mod) % mod
else:
    AE = [0] + AE + [0]
    mc = 0
    l = -2
    r = -2
    for (i, a) in enumerate(AE[1:], 1):
        if a == -1:
            if AE[i - 1] != -1:
                l = AE[i - 1]
            mc += 1
        else:
            r = AE[i]
            if AE[i - 1] == a:
                ans = 0
                break
            if mc:
                if not l or not r:
                    ans = ans * pow(K - 1, mc, mod) % mod
                elif l == r:
                    ans = ans * dp2[mc] % mod
                else:
                    ans = ans * (dp2[mc] * dif + dp1[mc]) % mod
            mc = 0
print(ans)
