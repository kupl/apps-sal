K = 32
P = 998244353
pa = (1 << 30) - (1 << 30) % P
M = []
(N, S) = map(int, input().split())
m = int(('1' * 2 + '0' * 30) * (S + 1), 2)
mm = 1 << K * S
mmm = (1 << K) - 1
A = [int(a) for a in input().split()]
s = 0
ans = 0
for a in A:
    s += mm
    s += s >> a * K
    s -= ((s & m) >> 30) * pa
    ans += s & mmm
print(ans % P)
