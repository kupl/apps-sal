K = 96
N, S = map(int, input().split())
A = [int(a) for a in input().split()]
P = 998244353
pa = (1 << 64) - ((1 << 64) % P)
m = int(("1" * 32 + "0" * 64) * 3030, 2)
modP = lambda x: x - ((x & m) >> 64) * pa
s = 1 << K * S
for a in A:
    s = 2 * s + (s >> K * a)
    s = modP(s)
print((s & ((1 << K) - 1)) % P)
