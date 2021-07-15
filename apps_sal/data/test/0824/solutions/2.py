mod = 10 ** 9 + 7

F, inv, iF = [1,1], [0, 1], [1, 1]

for i in range(2, 200005):
    F.append(F[-1] * i % mod)
    inv.append(inv[mod%i] * (mod - mod // i) % mod)
    iF.append(iF[-1] * inv[-1] % mod)

def C(n, k):
    if k < 0 or k > n:
        return  0
    return  F[n] * iF[k] *  iF[n - k]

s = input()
open, close = 0, s.count(')')

ans = 0

for c in s:
    if c == '(':
        open += 1
        ans += C(close + open - 1, open)
    else:
        close -= 1

print(ans % mod)
