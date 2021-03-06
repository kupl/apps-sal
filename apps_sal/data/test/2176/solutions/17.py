import sys
mod = 998244353
fact = [1]
for i in range(1, 300001):
    fact.append(fact[-1] * i % mod)
data = []
num = int(sys.stdin.readline())
l = []
for _ in range(num):
    temp = [int(i) for i in sys.stdin.readline().split()]
    data.append((temp[0] << 20) + temp[1])
    l.append(temp[1])
ans = 0
l.sort()
last = -1
tot = 1
run = 0
for p in l:
    if p == last:
        run += 1
    else:
        tot = tot * fact[run] % mod
        run = 1
        last = p
tot = tot * fact[run] % mod
ans += tot
data.sort()
f = [i >> 20 for i in data]
last = -1
tot = 1
run = 0
for p in f:
    if p == last:
        run += 1
    else:
        tot = tot * fact[run] % mod
        run = 1
        last = p
tot = tot * fact[run] % mod
ans += tot
pow2m1 = (1 << 20) - 1
sor = True
for i in range(num - 1):
    if data[i] & pow2m1 > data[i + 1] & pow2m1:
        sor = False
        break
if sor:
    last = -1
    tot = 1
    run = 0
    for p in data:
        if p == last:
            run += 1
        else:
            tot = tot * fact[run] % mod
            run = 1
            last = p
    tot = tot * fact[run] % mod
    ans -= tot
q = fact[num]
print((q - ans) % 998244353)
