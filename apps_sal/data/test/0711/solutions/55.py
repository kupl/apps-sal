MOD = 10**9 + 7
class mint:
    def __init__(self, i):
        self.i = i
    def __add__(self, m):
        t = self.i + (m.i if isinstance(m, mint) else m)
        if t > MOD:
            t -= MOD
        return mint(t)
    def __radd__(self, m):
        t = self.i + (m.i if isinstance(m, mint) else m)
        if t > MOD:
            t -= MOD
        return mint(t)
    def __mul__(self, m):
        return mint(self.i * (m.i if isinstance(m, mint) else m) % MOD)
    def __sub__(self, m):
        t = self.i - (m.i if isinstance(m, mint) else (m % MOD))
        if t < 0:
            t += MOD
        return mint(t)
    def __pow__(self, m):
        i = self.i
        return mint(pow(i, m, MOD))
    def __truediv__(self, m):
        return mint(self.i * pow(m, MOD - 2, MOD) % MOD)
    def __repr__(self):
        return repr(self.i)

fact_range = 10**6
facts = [1] * (fact_range + 1)
for i in range(0, fact_range):
    facts[i+1] = facts[i] * (i + 1) % MOD

ifacts = [1] * (fact_range + 1)
ifacts[fact_range] = pow(facts[fact_range], MOD - 2, MOD)
for i in range(fact_range, 0, -1):
    ifacts[i-1] = ifacts[i] * i % MOD

def comb(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return facts[n] * ifacts[n-k] % MOD * ifacts[k] % MOD

n, m = list(map(int, input().split()))
d = []
p = 2
while p < 10 ** 5:
    cnt = 0
    while m % p == 0:
        m //= p
        cnt += 1
    if cnt > 0:
        d.append(cnt)
    p += 1
if m > 1:
    d.append(1)
ans = mint(1)
for c in d:
    ans *= comb(n - 1 + c, c)
print(ans)

