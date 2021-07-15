s = input()
t = input()

base = 3
MOD = 1004535809

def rolling_hash(s, base, MOD):
    l = len(s)
    h = [0]*(l + 1)
    for i in range(l):
        h[i+1] = (h[i] * base + ord(s[i])) % MOD
    return h

s = s * ((len(t) + len(s) - 1)//len(s) * 2)
rh0 = rolling_hash(s, base, MOD)
B = 0
for c in t:
    B = (B * base + ord(c)) % MOD
N = len(s)//2
M = len(t)
R = [0]*N
L = pow(base, M, MOD)
r = 0
for i in range(N):
    if (rh0[i+M] - rh0[i]*L) % MOD == B:
        R[i] = 1
if not any(R):
    print(0)
    return

S = []
for i in range(N):
    if R[i-M] and R[i] == 0:
        S.append((i - M) % N)
if not S:
    print(-1)
    return

ans = 0
for v in S:
    d = 1
    while R[v-M]:
        d += 1
        v = (v - M) % N
    ans = max(ans, d)
print(ans)
