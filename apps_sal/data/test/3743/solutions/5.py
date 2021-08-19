import sys
readline = sys.stdin.readline


def prf(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1:
        pf[m] = 1
    return pf


N = int(readline())
Pf = prf(N)
ans = 1
if len(Pf) == 1:
    ans = list(Pf.keys())[0]
print(ans)
