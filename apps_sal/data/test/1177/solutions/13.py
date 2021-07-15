def setM():
    k = K2 // 2
    while k:
        m = int(("1" * (K2 - k) + "0" * (K2 + k)) * 3001, 2)
        M.append((k, m, ~m, (1 << K2 + k) % P))
        k //= 2
        break

def modp(n):
    for k, m, tm, a in M:
        n = (n & tm) + ((n & m) >> K2 + k) * a
    return n

K = 64
K2 = K // 2
P = 998244353
mm = (1 << K * 3001) - 1
mmm = (1 << K) - 1
M = []
setM()
N, S = map(int, input().split())
A = [int(a) for a in input().split()]
s = 0
ans = 0
for a in A:
    s += 1
    s += s << a * K
    s &= mm
    s = modp(s)
    ans += (s >> S * K) & mmm

print(ans % P)
