K = 32
P = 998244353
m = int(("1" * 2 + "0" * 30) * 3001, 2)
mm = (1 << K * 3001) - 1
mmm = (1 << K) - 1
pa = (1 << 30) - ((1 << 30) % P)

M = []
N, S = map(int, input().split())
A = [int(a) for a in input().split()]
s = 0
ans = 0
for a in A:
    s += 1
    s += s << a * K
    s &= mm
    s -= ((s & m) >> 30) * pa
    ans += (s >> S * K) & mmm

print(ans % P)
